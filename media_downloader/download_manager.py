"""
Download management for the Media Downloader application.
Handles thread-based downloading, progress tracking, pause/stop functionality.
"""

import tkinter as tk
import threading
import time
import os
import json
from datetime import datetime, timedelta

from download_core import download_with_ydl, DownloadError
from state_manager import update_status, update_status_and_progress, log_message, update_control_buttons, update_error_log_ui


def toggle_pause(app):
    """Toggles the pause state."""
    if app.is_downloading:
        if app.pause_requested.is_set():
            app.pause_requested.clear()
            update_status(app, "Download resumed.")
        else:
            app.pause_requested.set()
            update_status(app, "Download paused. Hit RESUME to continue.")
        
        app.msg_queue.put(('update_buttons', None))


def request_stop(app):
    """Sets the stop flag to terminate the download session."""
    if app.is_downloading:
        app.stop_requested.set()
        if app.pause_requested.is_set():
            app.pause_requested.clear()
        update_status(app, "STOP request received. Terminating current download and session...")
        app.stop_button.configure(state=tk.DISABLED)


def start_download_thread(app):
    """
    Initiates the main download process by creating and starting 
    a non-blocking thread, after validating input URLs.
    """
    if app.is_downloading:
        log_message(app, "[WARNING] A download is already in progress.")
        return

    urls_raw = app.url_text.get("1.0", tk.END).strip()
    
    # Split input by line and filter out empty strings
    urls = [u.strip() for u in urls_raw.splitlines() if u.strip()]
    
    if not urls:
        update_status(app, "Please paste one or more valid URLs to begin.")
        return

    log_message(app, f"Starting download session for {len(urls)} URL(s)...")
    
    # Reset error log for the new session
    app.failed_urls = []
    app.msg_queue.put(('update_error_log', None))
    
    app.is_downloading = True
    app.stop_requested.clear()
    app.pause_requested.clear()
    app.msg_queue.put(('update_buttons', None))
    
    # Create and start the thread, passing the list of URLs to the worker
    app.download_thread = threading.Thread(
        target=download_worker, 
        args=(app, urls), 
        daemon=True
    )
    app.download_thread.start()


def progress_hook(app, d):
    """Custom progress hook adapted for the GUI environment, providing detailed status and progress bar updates."""
    
    # 1. Stop Check
    if app.stop_requested.is_set():
        raise DownloadError("Download session terminated by user.")

    # 2. Pause Check
    while app.pause_requested.is_set():
        time.sleep(0.5)
        
    # Get the video title. Fallback to 'Unknown Media' if not available.
    title = d.get('info_dict', {}).get('title', 'Unknown Media')
    # Truncate title for cleaner display in the status bar
    display_title = title[:50] + '...' if len(title) > 50 else title
    
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes')
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        
        if total_bytes and downloaded_bytes:
            percent_float = (downloaded_bytes / total_bytes) * 100
            percent_int = int(percent_float)
            
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            
            status_msg = f"Downloading: '{display_title}' - {percent_int}% at {speed} ETA: {eta}"
            update_status_and_progress(app, status_msg, percent_int, mode='determinate')
        else:
             # Fallback for streams/downloads where total size is unknown
             percent = d.get('_percent_str', 'N/A')
             speed = d.get('_speed_str', 'N/A')
             eta = d.get('_eta_str', 'N/A')
             status_msg = f"Downloading: '{display_title}' - {percent} at {speed} ETA: {eta}"
             update_status_and_progress(app, status_msg, 0, mode='indeterminate')
             
    elif d['status'] == 'postprocessing':
        status_msg = f"Post-processing: '{display_title}' (Merging/Converting...)"
        # Use indeterminate mode for post-processing as percentage is usually unavailable
        update_status_and_progress(app, status_msg, 0, mode='indeterminate')
        
    elif d['status'] == 'finished':
        filename = d.get('filename', 'Unknown File')
        log_message(app, f"  >> FINISHED: {os.path.basename(filename)}")
        update_status_and_progress(app, f"Merge/Conversion complete for {os.path.basename(filename)}", 100, mode='determinate')
    
    elif d['status'] == 'error':
        log_message(app, f"  >> ERROR: {d.get('error', 'Unknown Error')}")


def download_worker(app, urls):
    """The function run in the separate thread to handle yt-dlp downloads."""
    
    # Load quality map from config
    import os
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    QUALITY_MAP = config['quality_map']
    
    try:
        output_dir = app.output_dir.get()
        quality_key = app.quality_var.get()
        download_type = app.download_type.get()
        
        format_string = QUALITY_MAP.get(quality_key, QUALITY_MAP['video_best'])
        
        # 1. Create directory if needed
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log_message(app, f"Created output directory: {output_dir}")

        log_message(app, f"Download Type: {download_type} | Format: {quality_key} (String: {format_string})")
        
        ydl_opts = {
            'format': format_string,
            'outtmpl': os.path.join(output_dir, '%(title)s - %(uploader)s - %(id)s.%(ext)s'),
            'restrictfilenames': True,
            'noplaylist': False, 
            'progress_hooks': [lambda d: progress_hook(app, d)],
            'quiet': True, 
            'no_warnings': True,
            'force_generic_extractor': False,
        }
        
        # 2. Configure Download Type
        if download_type == 'Audio':
            ext = 'mp3' if quality_key == 'audio_mp3' else 'opus' 
            ydl_opts.update({
                'extract_audio': True,
                'audioformat': ext,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': ext,
                    'preferredquality': '192', 
                }],
                'outtmpl': os.path.join(output_dir, '%(title)s - %(uploader)s - %(id)s.%(ext)s'),
            })
        else: # Video
             ydl_opts['merge_output_format'] = 'mp4'
             
        # 3. Configure Date Filter
        days_str = app.date_filter_days.get().strip()
        if days_str and days_str.isdigit():
            days = int(days_str)
            cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
            ydl_opts['dateafter'] = cutoff_date
            log_message(app, f"Filtering: Skipping media uploaded before {cutoff_date} ({days} days ago).")

        # 4. Configure Playlist/Index Filters
        start_index_str = app.playlist_start_var.get().strip()
        end_index_str = app.playlist_end_var.get().strip()

        if start_index_str and start_index_str.isdigit() and int(start_index_str) > 0:
            ydl_opts['playlist_start'] = int(start_index_str)
            log_message(app, f"Collection: Starting download from index {start_index_str}.")
        
        if end_index_str and end_index_str.isdigit():
            ydl_opts['playlist_end'] = int(end_index_str)
            log_message(app, f"Collection: Ending download at index {end_index_str}.")

        # 5. Configure Skip Shorts
        if app.skip_shorts_var.get():
            ydl_opts['match_filter'] = lambda info, incomplete: None if 'shorts/' in info['webpage_url'] else None
            log_message(app, "Filtering: Attempting to skip short-form media.")

        # --- Execute Download ---
        
        for i, url in enumerate(urls):
            if app.stop_requested.is_set():
                log_message(app, "\n[SESSION TERMINATED] Stop flag detected. Halting further URL processing.")
                break
                
            log_message(app, f"\n[{i+1}/{len(urls)}] Processing URL: {url}")
            # Reset progress bar to 0 before a new item starts
            update_status_and_progress(app, f"Starting analysis for URL {i+1}...", 0, 'indeterminate')
            
            while app.pause_requested.is_set():
                update_status(app, f"PAUSED before processing URL {i+1}. Hit RESUME to continue.")
                time.sleep(0.5)

            # Use centralized downloader utility to perform the yt-dlp call
            download_with_ydl([url], ydl_opts, lambda d: progress_hook(app, d), lambda msg: log_message(app, msg), app.stop_requested, app.pause_requested, app.failed_urls)

    except Exception as e:
        log_message(app, f"Fatal error during download process: {e}")
        
    finally:
        if app.stop_requested.is_set():
             final_message = "\n--- Download Session TERMINATED by user. ---"
        else:
             final_message = "\n--- All Downloads Finished! ---"
        
        app.msg_queue.put(('log', final_message))
        app.msg_queue.put(('update_error_log', None))
        
        # Reset status and progress bar
        update_status_and_progress(app, "Download session complete. Ready.", 0, 'determinate')
        
        # Reset final state
        app.is_downloading = False
        app.stop_requested.clear()
        app.pause_requested.clear()
        app.msg_queue.put(('update_buttons', None))
