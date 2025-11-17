import os
import time
from yt_dlp import YoutubeDL, DownloadError


def download_with_ydl(urls, ydl_opts, progress_hook, log_func, stop_event, pause_event, failed_urls=None):
    """Downloads a list of URLs using yt-dlp using the provided options.

    Args:
        urls: list of URL strings
        ydl_opts: options for YoutubeDL
        progress_hook: callable to receive progress dicts
        log_func: callable to log messages (e.g., app._log)
        stop_event: threading.Event to signal stop
        pause_event: threading.Event to signal pause
        failed_urls: list to append failed URLs
    """

    if failed_urls is None:
        failed_urls = []

    for i, url in enumerate(urls):
        if stop_event.is_set():
            log_func("\n[SESSION TERMINATED] Stop flag detected. Halting further URL processing.")
            break

        log_func(f"\n[{i+1}/{len(urls)}] Processing URL: {url}")

        while pause_event.is_set():
            log_func(f"PAUSED before processing URL {i+1}. Hit RESUME to continue.")
            time.sleep(0.5)

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except DownloadError as e:
            if "Download session terminated by user" in str(e):
                log_func(f"\n[SESSION TERMINATED] User stopped download {i+1}.")
                stop_event.set()
                break
            else:
                error_msg = str(e).splitlines()[0]
                log_func(f"[ERROR] Failed to download: {url}. The link may be private or incorrect. Error: {error_msg}")
                failed_urls.append(url)
        except Exception as e:
            log_func(f"[FATAL] An unexpected error occurred for {url}: {e}")
            failed_urls.append(url)

    return failed_urls
