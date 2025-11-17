"""
Spotify downloader module for downloading songs, albums, and playlists.
Uses spotdl library for conversion and yt-dlp for audio extraction.
"""

import os
import subprocess
import threading
import json
from datetime import datetime


def check_spotdl_installed():
    """Check if spotdl is installed."""
    try:
        import spotdl
        return True
    except ImportError:
        return False


def install_spotdl():
    """Install spotdl package."""
    try:
        subprocess.check_call([
            'python', '-m', 'pip', 'install', 'spotdl', '-q'
        ])
        return True
    except subprocess.CalledProcessError:
        return False


def validate_spotify_url(url):
    """Validate if the URL is a valid Spotify link."""
    valid_prefixes = [
        'https://open.spotify.com/track/',
        'https://open.spotify.com/album/',
        'https://open.spotify.com/playlist/',
    ]
    return any(url.startswith(prefix) for prefix in valid_prefixes)


def get_spotify_item_type(url):
    """Determine the type of Spotify item from URL."""
    if '/track/' in url:
        return 'Track'
    elif '/album/' in url:
        return 'Album'
    elif '/playlist/' in url:
        return 'Playlist'
    return 'Unknown'


def spotify_download_worker(app, urls, output_dir, audio_format):
    """
    Worker function to download Spotify content.
    Runs in separate thread to avoid blocking UI.
    """
    from state_manager import log_message, update_status, update_status_and_progress
    
    try:
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log_message(app, f"[Spotify] Created output directory: {output_dir}")
        
        total_urls = len(urls)
        failed_urls = []
        
        for idx, url in enumerate(urls, 1):
            # Check if stop requested
            if app.spotify_stop_event.is_set():
                log_message(app, "[Spotify] Download stopped by user")
                break
            
            if not url.strip():
                continue
            
            item_type = get_spotify_item_type(url)
            log_message(app, f"\n[{idx}/{total_urls}] Downloading {item_type}: {url}")
            
            try:
                # Build spotdl command
                cmd = [
                    'spotdl', 'download',
                    url,
                    '--output', output_dir,
                    '--audio', audio_format,
                    '--cookie-file', os.path.expanduser('~/.spotify_cache'),
                ]
                
                # Run spotdl
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                
                if result.returncode == 0:
                    log_message(app, f"  >> Successfully downloaded {item_type}")
                    progress = int((idx / total_urls) * 100)
                    update_status_and_progress(app, f"Downloaded {idx}/{total_urls}", progress, 'determinate')
                else:
                    error_msg = result.stderr if result.stderr else "Unknown error"
                    log_message(app, f"  >> ERROR: {error_msg}")
                    failed_urls.append(url)
            
            except subprocess.TimeoutExpired:
                log_message(app, f"  >> ERROR: Download timed out")
                failed_urls.append(url)
            except Exception as e:
                log_message(app, f"  >> ERROR: {str(e)}")
                failed_urls.append(url)
        
        # Final status
        success_count = total_urls - len(failed_urls)
        if failed_urls:
            app.spotify_failed_urls = failed_urls
            log_message(app, f"\n[Spotify] Download complete: {success_count}/{total_urls} successful")
            log_message(app, f"[Spotify] {len(failed_urls)} failed URL(s) - see Error Logger")
        else:
            log_message(app, f"\n[Spotify] All {success_count} item(s) downloaded successfully!")
        
        update_status(app, "Ready")
        update_status_and_progress(app, f"Completed: {success_count}/{total_urls}", 100, 'determinate')
    
    except Exception as e:
        log_message(app, f"[Spotify] FATAL ERROR: {str(e)}")
        update_status(app, "Error - check logs")


def start_spotify_download_thread(app):
    """Start the Spotify download in a separate thread."""
    from state_manager import log_message, update_status
    
    urls_text = app.spotify_url_text.get("1.0", "end-1c").strip()
    if not urls_text:
        log_message(app, "[Spotify] No URLs provided")
        return
    
    output_dir = app.spotify_output_dir.get().strip()
    if not output_dir:
        log_message(app, "[Spotify] No output directory specified")
        return
    
    audio_format = app.spotify_format_var.get()
    if not audio_format:
        log_message(app, "[Spotify] No audio format selected")
        return
    
    # Parse URLs
    urls = [line.strip() for line in urls_text.split('\n') if line.strip()]
    invalid_urls = [url for url in urls if not validate_spotify_url(url)]
    
    if invalid_urls:
        log_message(app, f"[Spotify] ERROR: {len(invalid_urls)} invalid URL(s):")
        for url in invalid_urls:
            log_message(app, f"  >> {url}")
        return
    
    # Clear stop event and failed URLs
    app.spotify_stop_event.clear()
    app.spotify_failed_urls = []
    
    # Disable start button, enable pause/stop
    app.spotify_start_button.config(state='disabled')
    app.spotify_stop_button.config(state='normal')
    
    update_status(app, f"Downloading {len(urls)} Spotify item(s)...")
    
    # Start download thread
    thread = threading.Thread(
        target=spotify_download_worker,
        args=(app, urls, output_dir, audio_format),
        daemon=True
    )
    thread.start()


def stop_spotify_download(app):
    """Stop the Spotify download."""
    from state_manager import log_message, update_status
    
    app.spotify_stop_event.set()
    log_message(app, "[Spotify] Stop requested...")
    update_status(app, "Stopping...")
    
    # Re-enable start button, disable stop button
    app.spotify_start_button.config(state='normal')
    app.spotify_stop_button.config(state='disabled')


def open_spotify_output_folder(app):
    """Open the Spotify output folder in file explorer."""
    import subprocess
    
    output_dir = app.spotify_output_dir.get().strip()
    if not output_dir or not os.path.exists(output_dir):
        return
    
    try:
        if os.name == 'nt':  # Windows
            os.startfile(output_dir)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', output_dir])
    except Exception as e:
        pass
