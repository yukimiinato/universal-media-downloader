import os
import sys
import subprocess
import time

# Try to import yt-dlp
try:
    from yt_dlp import YoutubeDL, DownloadError
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    class DummyYoutubeDL:
        pass
    YoutubeDL = DummyYoutubeDL
    DownloadError = Exception


def restart_program():
    """Restart the current program."""
    os.execl(sys.executable, sys.executable, *sys.argv)


def check_for_ffmpeg():
    """Checks if the FFmpeg executable is available in the system's PATH."""
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def handle_yt_dlp_install():
    """Attempts to install yt-dlp via pip and restarts if successful."""
    print("--- Universal Media Downloader Dependency Check ---")
    print("[STATUS] Python dependency 'yt-dlp' not found.")
    print("Attempting installation via pip. This may take a moment...")

    pip_command = [sys.executable, "-m", "pip", "install", "yt-dlp"]

    try:
        result = subprocess.run(
            pip_command,
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=False
        )

        if result.returncode == 0:
            print("\n[SUCCESS] 'yt-dlp' installed successfully!")
            print("Restarting application to load the new module and continue checks...")
            restart_program()
        else:
            print(f"\n[ERROR] Failed to install yt-dlp (Code: {result.returncode}).")
            print("--- Installation Output (Error/Warning) ---")
            print(result.stderr or result.stdout)
            print("-------------------------------------------")
            print("Please install 'yt-dlp' manually using 'pip install yt-dlp' and try again.")
            input("Press Enter to exit the application...")
            sys.exit(1)

    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred during installation: {e}")
        input("Press Enter to exit the application...")
        sys.exit(1)


def install_ffmpeg_via_winget():
    """Attempts to install FFmpeg using Winget (Windows Package Manager)."""
    print("\n[STATUS] Attempting automatic FFmpeg installation via Winget...")

    try:
        subprocess.run(['winget', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] Winget command not found. Falling back to manual install instructions.")
        return False

    WINGET_FFMPEG_ID = "Gyan.FFmpeg"

    command = [
        "winget", "install",
        "--id", WINGET_FFMPEG_ID,
        "-e",
        "--accept-package-agreements",
        "--accept-source-agreements"
    ]

    try:
        process = subprocess.run(
            command,
            check=False,
            text=True,
            capture_output=True,
            encoding='utf-8'
        )

        if process.returncode == 0:
            print("[SUCCESS] Winget installation command executed.")
            return True
        else:
            print(f"[FAIL] Winget installation failed (Exit Code {process.returncode}).")
            print(f"STDERR: {process.stderr.strip()}")
            return False

    except Exception as e:
        print(f"[FATAL] An unexpected error occurred during Winget execution: {e}")
        return False


def install_ffmpeg_via_apt():
    """Attempts to install FFmpeg on Linux via apt package manager."""
    print("\n[STATUS] Attempting automatic FFmpeg installation via apt...")

    try:
        subprocess.run(['apt', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] apt command not found. System may not be Debian/Ubuntu based.")
        return False

    try:
        print("[INFO] Updating package list (may require sudo)...")
        update_cmd = ['sudo', 'apt', 'update']
        update_result = subprocess.run(update_cmd, capture_output=True, text=True, check=False)

        if update_result.returncode != 0:
            print("[FAIL] Failed to update package list.")
            return False

        print("[INFO] Installing FFmpeg (may require sudo)...")
        install_cmd = ['sudo', 'apt', 'install', '-y', 'ffmpeg']
        install_result = subprocess.run(install_cmd, capture_output=True, text=True, check=False)

        if install_result.returncode == 0:
            print("[SUCCESS] FFmpeg installed successfully via apt.")
            return True
        else:
            print(f"[FAIL] apt installation failed (Exit Code {install_result.returncode}).")
            return False

    except Exception as e:
        print(f"[FATAL] An unexpected error occurred during apt installation: {e}")
        return False


def install_ffmpeg_via_dnf():
    """Attempts to install FFmpeg on Linux via dnf package manager (Fedora/RHEL)."""
    print("\n[STATUS] Attempting automatic FFmpeg installation via dnf...")

    try:
        subprocess.run(['dnf', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] dnf command not found. System may not be Fedora/RHEL based.")
        return False

    try:
        print("[INFO] Installing FFmpeg (may require sudo)...")
        install_cmd = ['sudo', 'dnf', 'install', '-y', 'ffmpeg']
        install_result = subprocess.run(install_cmd, capture_output=True, text=True, check=False)

        if install_result.returncode == 0:
            print("[SUCCESS] FFmpeg installed successfully via dnf.")
            return True
        else:
            print(f"[FAIL] dnf installation failed (Exit Code {install_result.returncode}).")
            return False

    except Exception as e:
        print(f"[FATAL] An unexpected error occurred during dnf installation: {e}")
        return False


def install_ffmpeg_via_brew():
    """Attempts to install FFmpeg on macOS via Homebrew."""
    print("\n[STATUS] Attempting automatic FFmpeg installation via Homebrew...")

    try:
        subprocess.run(['brew', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] Homebrew not found. Please install it from https://brew.sh")
        return False

    try:
        print("[INFO] Installing FFmpeg via Homebrew...")
        install_cmd = ['brew', 'install', 'ffmpeg']
        install_result = subprocess.run(install_cmd, capture_output=True, text=True, check=False)

        if install_result.returncode == 0:
            print("[SUCCESS] FFmpeg installed successfully via Homebrew.")
            return True
        else:
            print(f"[FAIL] Homebrew installation failed (Exit Code {install_result.returncode}).")
            return False

    except Exception as e:
        print(f"[FATAL] An unexpected error occurred during Homebrew installation: {e}")
        return False


def handle_ffmpeg_check():
    """Checks for FFmpeg and attempts platform-specific automatic installation."""
    print("--- Universal Media Downloader Dependency Check ---")
    print("[STATUS] Python dependency 'yt-dlp' is OK.")

    if check_for_ffmpeg():
        print("[SUCCESS] FFmpeg is already installed. Launching GUI.")
        return

    print("[CRITICAL] FFmpeg not found. Attempting automatic installation...")

    if os.name == 'nt' or sys.platform == 'win32':
        print("[PLATFORM] Detected Windows")
        if install_ffmpeg_via_winget():
            time.sleep(1)
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return
            else:
                print("[WARNING] Installation complete, but FFmpeg not yet in PATH.")
                print("Please restart the application.")
                input("Press Enter to exit...")
                sys.exit(0)

    elif sys.platform.startswith('linux'):
        print("[PLATFORM] Detected Linux")
        if install_ffmpeg_via_apt():
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return

        if install_ffmpeg_via_dnf():
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return

        print("[FAIL] Automatic installation failed on both apt and dnf.")

    elif sys.platform == 'darwin':
        print("[PLATFORM] Detected macOS")
        if install_ffmpeg_via_brew():
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return
            else:
                print("[WARNING] Installation complete, but FFmpeg not yet in PATH.")
                print("Please restart the application.")
                input("Press Enter to exit...")
                sys.exit(0)

    print("\n[CRITICAL ERROR] FFmpeg is required to merge video/audio streams and convert formats.")
    print("--- Manual Installation Instructions ---")

    if os.name == 'nt' or sys.platform == 'win32':
        print("Windows:")
        print("  1. Download FFmpeg: https://ffmpeg.org/download.html")
        print("  2. Extract and add directory to PATH")
        print("  3. Restart this application")
    elif sys.platform.startswith('linux'):
        print("Linux (Debian/Ubuntu):")
        print("  1. Run: sudo apt update && sudo apt install ffmpeg")
        print("Linux (Fedora/RHEL):")
        print("  1. Run: sudo dnf install ffmpeg")
        print("Linux (Arch):")
        print("  1. Run: sudo pacman -S ffmpeg")
    elif sys.platform == 'darwin':
        print("macOS:")
        print("  1. Install Homebrew: https://brew.sh")
        print("  2. Run: brew install ffmpeg")

    print("\nOnce installed, restart this application.")
    print("---------------------------------------------")
    input("Press Enter to exit...")
    sys.exit(1)
