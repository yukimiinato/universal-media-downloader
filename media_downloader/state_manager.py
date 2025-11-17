"""
State management for the Media Downloader application.
Handles logging, status updates, error tracking, and UI state synchronization.
"""

import tkinter as tk


def log_message(app, message):
    """Thread-safe logging to the Download Log Text widget."""
    app.msg_queue.put(('log', message))


def update_status(app, message):
    """Thread-safe status bar update (used for non-download status)."""
    app.msg_queue.put(('status', message))


def update_status_and_progress(app, status_msg, percentage, mode='determinate'):
    """Thread-safe update for both status text and progress bar."""
    app.msg_queue.put(('progress_update', (status_msg, percentage, mode)))


def update_error_log_ui(app):
    """Updates the Error Logger text widget with the list of failed URLs."""
    app.error_text.config(state=tk.NORMAL)
    app.error_text.delete("1.0", tk.END)
    
    if app.failed_urls:
        content = f"--- {len(app.failed_urls)} Failed URLs ---\n\n"
        content += "\n".join(app.failed_urls)
        app.error_text.insert(tk.END, content)
        app.copy_errors_button.config(state=tk.NORMAL)
    else:
        app.error_text.insert(tk.END, "No errors logged yet!")
        app.copy_errors_button.config(state=tk.DISABLED)
        
    app.error_text.config(state=tk.DISABLED)


def copy_failed_urls(app):
    """Copies the list of failed URLs to the clipboard."""
    if app.failed_urls:
        links = "\n".join(app.failed_urls)
        app.master.clipboard_clear()
        app.master.clipboard_append(links)
        update_status(app, f"Copied {len(app.failed_urls)} failed URLs to clipboard!")
    else:
        update_status(app, "No failed URLs to copy.")


def update_control_buttons(app):
    """Updates the state and text of the control buttons."""
    if app.is_downloading:
        app.start_button.configure(state=tk.DISABLED)
        app.pause_button.configure(state=tk.NORMAL)
        app.stop_button.configure(state=tk.NORMAL)
        
        if app.pause_requested.is_set():
            app.pause_button.configure(text="RESUME", style='Start.TButton')
        else:
            app.pause_button.configure(text="PAUSE", style='Accent.TButton')

    else:
        app.start_button.configure(text="START DOWNLOAD", state=tk.NORMAL)
        app.pause_button.configure(text="PAUSE", state=tk.DISABLED, style='Accent.TButton')
        app.stop_button.configure(state=tk.DISABLED)


def update_quality_options(app):
    """Updates the quality dropdown based on download type (Video/Audio)."""
    import json
    import os
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    QUALITY_MAP = config['quality_map']
    
    current_type = app.download_type.get()
    if current_type == 'Video':
        video_qualities = [k for k in QUALITY_MAP.keys() if k.startswith('video')]
        app.quality_menu.configure(values=video_qualities)
        app.quality_var.set(video_qualities[0] if video_qualities else 'video_best')
    else:  # Audio
        audio_qualities = [k for k in QUALITY_MAP.keys() if k.startswith('audio')]
        app.quality_menu.configure(values=audio_qualities)
        app.quality_var.set(audio_qualities[0] if audio_qualities else 'audio_mp3')
