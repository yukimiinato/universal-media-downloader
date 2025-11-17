#!/usr/bin/env python3
"""
Launcher script for the Universal Media Downloader v1.0.1
This script launches the media downloader application from the media_downloader package.
"""

import os
import sys

# Add the media_downloader package to the path
package_dir = os.path.join(os.path.dirname(__file__), 'media_downloader')
sys.path.insert(0, package_dir)

# Import and run the application
from main import MediaDownloaderApp, handle_yt_dlp_install, check_for_ffmpeg, handle_ffmpeg_check, YT_DLP_AVAILABLE
import tkinter as tk

if __name__ == "__main__":
    # 1. Check for Python Dependency (yt-dlp)
    if not YT_DLP_AVAILABLE:
        handle_yt_dlp_install() 
    
    # 2. Check for System Dependency (FFmpeg)
    if not check_for_ffmpeg():
        handle_ffmpeg_check()

    # If both checks pass, launch the GUI
    root = tk.Tk()
    app = MediaDownloaderApp(root)
    root.mainloop()
