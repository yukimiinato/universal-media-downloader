import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
from queue import Queue
import sys
import subprocess
import time 
from datetime import datetime, timedelta 

# Import themes from the themes module (instead of defining them locally)
from themes import THEMES, get_all_theme_names

# Try to import yt-dlp right away
try:
    from yt_dlp import YoutubeDL, DownloadError 
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    class DummyYoutubeDL: 
        pass
    YoutubeDL = DummyYoutubeDL
    DownloadError = Exception

# --- Core yt-dlp Configuration ---

QUALITY_MAP = {
    # Video Formats (Requires FFmpeg for merging and mp4 conversion)
    'video_best': 'bestvideo+bestaudio/best',
    'video_1080p': 'bestvideo[height<=1080]+bestaudio/best',
    'video_720p': 'bestvideo[height<=720]+bestaudio/best',
    'video_480p': 'bestvideo[height<=480]+bestaudio/best',
    # Audio Formats (Requires FFmpeg for format conversion like mp3)
    'audio_mp3': 'bestaudio/best',
    'audio_opus': 'bestaudio/best',
}

# --- DEPENDENCY CHECK/INSTALL FOR CONSOLE STARTUP ---

def restart_program():
    """Restarts the current Python script."""
    os.execl(sys.executable, sys.executable, *sys.argv)

def check_for_ffmpeg():
    """Checks if the FFmpeg executable is available in the system's PATH."""
    try:
        # Check if the command runs successfully (no output needed, just return code)
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

    # Check for winget availability 
    try:
        subprocess.run(['winget', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] Winget command not found. Falling back to manual install instructions.")
        return False

    # Common ID for FFmpeg static build
    WINGET_FFMPEG_ID = "Gyan.FFmpeg"
    
    # Non-interactive installation command
    command = [
        "winget", "install", 
        "--id", WINGET_FFMPEG_ID, 
        "-e", 
        "--accept-package-agreements", 
        "--accept-source-agreements"
    ]
    
    try:
        # Run the installation command
        process = subprocess.run(
            command, 
            check=False, # We check return code and output manually
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
    
    # Check if apt is available
    try:
        subprocess.run(['apt', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] apt command not found. System may not be Debian/Ubuntu based.")
        return False
    
    try:
        # Update package list
        print("[INFO] Updating package list (may require sudo)...")
        update_cmd = ['sudo', 'apt', 'update']
        update_result = subprocess.run(update_cmd, capture_output=True, text=True, check=False)
        
        if update_result.returncode != 0:
            print("[FAIL] Failed to update package list.")
            return False
        
        # Install FFmpeg
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
    
    # Check if dnf is available
    try:
        subprocess.run(['dnf', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] dnf command not found. System may not be Fedora/RHEL based.")
        return False
    
    try:
        # Install FFmpeg
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
    
    # Check if brew is available
    try:
        subprocess.run(['brew', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("[FAIL] Homebrew not found. Please install it from https://brew.sh")
        return False
    
    try:
        # Install FFmpeg
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
    
    # Platform-specific installation attempts
    if os.name == 'nt' or sys.platform == 'win32':
        # --- Windows: Try Winget Auto-Install ---
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
        # --- Linux: Try apt or dnf ---
        print("[PLATFORM] Detected Linux")
        
        # Try apt first (Debian/Ubuntu)
        if install_ffmpeg_via_apt():
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return
        
        # Try dnf if apt failed (Fedora/RHEL)
        if install_ffmpeg_via_dnf():
            if check_for_ffmpeg():
                print("[SUCCESS] FFmpeg installed successfully. Launching GUI.")
                return
        
        # Fall through to manual instructions
        print("[FAIL] Automatic installation failed on both apt and dnf.")
    
    elif sys.platform == 'darwin':
        # --- macOS: Try Homebrew ---
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
    
    # --- Manual Installation Instructions (Fallback) ---
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


# --- GUI Application Class ---

class MediaDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Universal Media Downloader (yt-dlp)")
        master.geometry("800x800") 

        # Variables
        self.output_dir = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Videos", "Media_Downloads"))
        self.download_type = tk.StringVar(value='Video')
        self.quality_var = tk.StringVar(value='video_best')
        self.status_text = tk.StringVar(value="Ready to download.")
        self.is_downloading = False
        # `current_palette` holds the palette name only (e.g. 'Nord').
        # Mode (dark/light) is controlled independently by `current_mode` and the toggle button.
        self.current_palette = tk.StringVar(value='Nord')
        self.current_mode = 'dark'
        
        # Error Logger variable
        self.failed_urls = []
        
        # New Control Variables for Pause/Stop
        self.stop_requested = threading.Event() 
        self.pause_requested = threading.Event() 
        self.pause_requested.clear() 

        # Options Variables
        self.date_filter_days = tk.StringVar(value='') 
        self.skip_shorts_var = tk.BooleanVar(value=True) 
        self.playlist_start_var = tk.StringVar(value='1')
        self.playlist_end_var = tk.StringVar(value='') 
        
        self.msg_queue = Queue()

        # Initialize UI Components
        self.create_widgets()
        self.setup_bindings()
        
        self.apply_theme(self.current_mode)
        self._update_control_buttons() 
        self._update_quality_options()
        self._update_error_log_ui()
        
        self.master.after(100, self.check_queue)
        
    def create_widgets(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.main_frame = ttk.Frame(self.master, padding="20 20 20 20")
        self.main_frame.pack(fill='both', expand=True)

        title_control_frame = ttk.Frame(self.main_frame)
        title_control_frame.pack(fill='x', pady=(0, 20))

        # Updated Title
        self.title_label = ttk.Label(title_control_frame, text="Universal Media Downloader", style='Title.TLabel')
        self.title_label.pack(side=tk.LEFT)
        
        # Right side controls (Mode buttons and Theme dropdown)
        right_controls_frame = ttk.Frame(title_control_frame)
        right_controls_frame.pack(side=tk.RIGHT)
        
        self.toggle_button = ttk.Button(right_controls_frame, text="☀️", command=self.toggle_theme, style='Toggle.TButton', width=3)
        self.toggle_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Theme dropdown
        ttk.Label(right_controls_frame, text="Theme:").pack(side=tk.LEFT, padx=(0, 5))

        # Build a unique list of palette names (no Light/Dark suffix)
        all_theme_names = get_all_theme_names()
        palette_names = []
        for t in all_theme_names:
            base = t.split(' (')[0]
            if base not in palette_names:
                palette_names.append(base)
        palette_names.sort()

        # Combobox shows only palette names; mode is toggled by the button
        self.theme_menu = ttk.Combobox(right_controls_frame, textvariable=self.current_palette, values=palette_names, state='readonly', width=18)
        self.theme_menu.pack(side=tk.LEFT)
        self.theme_menu.bind('<<ComboboxSelected>>', self.on_palette_changed)

        # --- Input Section (Top) ---
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill='x', pady=10)
        
        ttk.Label(input_frame, text="Paste URLs (Video/Playlist, One per line, Supports many sites):").pack(anchor='w', pady=(0, 5))
        
        # URL Text Area (Bind right-click)
        self.url_text = tk.Text(input_frame, height=7, width=80, bd=0, relief="flat", font=('Inter', 10))
        self.url_text.pack(fill='x', expand=True)
        
        # --- Options Section (Middle) ---
        options_main_frame = ttk.Frame(self.main_frame)
        options_main_frame.pack(fill='x', pady=20)
        
        # Left Options Frame (Download Type, Quality)
        left_options_frame = ttk.Frame(options_main_frame)
        left_options_frame.pack(side=tk.LEFT, fill='x', expand=True, padx=(0, 10))

        # Download Type Radio Buttons
        ttk.Label(left_options_frame, text="Download Type:").grid(row=0, column=0, sticky='w', pady=5)
        
        type_frame = ttk.Frame(left_options_frame)
        type_frame.grid(row=1, column=0, columnspan=2, sticky='w', pady=(0, 10))
        
        self.video_radio = ttk.Radiobutton(type_frame, text="Video", variable=self.download_type, value='Video', command=self._update_quality_options, style='TRadiobutton')
        self.video_radio.pack(side=tk.LEFT, padx=(0, 15))
        
        self.audio_radio = ttk.Radiobutton(type_frame, text="Audio Only (MP3/Opus)", variable=self.download_type, value='Audio', command=self._update_quality_options, style='TRadiobutton')
        self.audio_radio.pack(side=tk.LEFT)

        # Quality Dropdown
        ttk.Label(left_options_frame, text="Quality/Format:").grid(row=2, column=0, sticky='w', pady=5)
        
        self.quality_menu = ttk.Combobox(left_options_frame, textvariable=self.quality_var, values=list(QUALITY_MAP.keys()), state='readonly', width=18)
        self.quality_menu.grid(row=3, column=0, columnspan=2, sticky='w')
        
        
        # Right Options Frame (Date/Skip Filters)
        right_options_frame = ttk.Frame(options_main_frame)
        right_options_frame.pack(side=tk.LEFT, fill='x', expand=True, padx=(10, 0))
        
        # Skip Shorts Checkbox 
        self.skip_shorts_check = ttk.Checkbutton(right_options_frame, text="Skip Short-form Media (e.g., Shorts)", variable=self.skip_shorts_var, style='TCheckbutton')
        self.skip_shorts_check.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)
        
        # Date Filter
        ttk.Label(right_options_frame, text="Skip media older than (days):").grid(row=1, column=0, sticky='w', pady=5)
        
        self.date_filter_entry = ttk.Entry(right_options_frame, textvariable=self.date_filter_days, width=5, font=('Inter', 10))
        self.date_filter_entry.grid(row=1, column=1, sticky='w')
        
        # Playlist Index Filters
        ttk.Label(right_options_frame, text="Collection Start Index:").grid(row=2, column=0, sticky='w', pady=5)
        self.playlist_start_entry = ttk.Entry(right_options_frame, textvariable=self.playlist_start_var, width=5, font=('Inter', 10))
        self.playlist_start_entry.grid(row=2, column=1, sticky='w')

        ttk.Label(right_options_frame, text="Collection End Index:").grid(row=3, column=0, sticky='w', pady=5)
        self.playlist_end_entry = ttk.Entry(right_options_frame, textvariable=self.playlist_end_var, width=5, font=('Inter', 10))
        self.playlist_end_entry.grid(row=3, column=1, sticky='w')

        # --- Output Path Section ---
        output_frame = ttk.Frame(self.main_frame)
        output_frame.pack(fill='x', pady=10)
        
        ttk.Label(output_frame, text="Output Folder:").grid(row=0, column=0, padx=(0, 10), sticky='w')
        
        # Output Entry (Bind right-click)
        self.output_entry = ttk.Entry(output_frame, textvariable=self.output_dir, width=40, font=('Inter', 10))
        self.output_entry.grid(row=0, column=1, sticky='ew', ipady=2) 
        
        self.output_button = ttk.Button(output_frame, text="Browse", command=self.select_output_dir, style='Accent.TButton')
        self.output_button.grid(row=0, column=2, padx=(10, 0), sticky='w')
        
        output_frame.grid_columnconfigure(1, weight=1) 


        # --- Control and Status Section ---
        control_frame = ttk.Frame(self.main_frame)
        control_frame.pack(fill='x', pady=(10, 20))

        # Start Button
        self.start_button = ttk.Button(control_frame, text="START DOWNLOAD", command=self.start_download_thread, style='Start.TButton')
        self.start_button.pack(side=tk.LEFT, expand=True, padx=5, ipady=5)
        
        # Pause/Resume Button
        self.pause_button = ttk.Button(control_frame, text="PAUSE", command=self.toggle_pause, style='Accent.TButton', state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, expand=True, padx=5, ipady=5)

        # Stop Button
        self.stop_button = ttk.Button(control_frame, text="STOP ALL", command=self.request_stop, style='Stop.TButton', state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, expand=True, padx=5, ipady=5)


        # Status Bar and Folder Button
        status_control_frame = ttk.Frame(self.main_frame)
        status_control_frame.pack(fill='x', pady=(0, 5))
        
        # Open Folder Button
        self.open_folder_button = ttk.Button(status_control_frame, text="📂 Open Output Folder", command=self.open_output_folder, style='Accent.TButton')
        self.open_folder_button.pack(side=tk.RIGHT, padx=(10, 0))

        self.status_bar = ttk.Frame(status_control_frame, style='Status.TFrame')
        self.status_bar.pack(side=tk.LEFT, fill='x', expand=True)
        
        self.status_label = ttk.Label(self.status_bar, textvariable=self.status_text, style='Status.TLabel', anchor='w')
        self.status_label.pack(fill='x', padx=10, pady=5)
        
        # --- Progress Bar ---
        self.progress_bar = ttk.Progressbar(self.main_frame, orient='horizontal', length=100, mode='determinate')
        self.progress_bar.pack(fill='x', pady=(0, 10))

        # --- Log and Error Tabs (ttk.Notebook) ---
        ttk.Label(self.main_frame, text="Session Logs:").pack(anchor='w', pady=(10, 5))
        
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True)

        # 1. Download Log Tab
        download_log_frame = ttk.Frame(self.notebook, padding="5")
        self.notebook.add(download_log_frame, text="Download Log")

        self.log_text = tk.Text(download_log_frame, height=10, bd=0, relief="flat", font=('Consolas', 9))
        self.log_text.pack(side="left", fill="both", expand=True)
        log_scrollbar = ttk.Scrollbar(download_log_frame, command=self.log_text.yview)
        log_scrollbar.pack(side="right", fill="y")
        self.log_text['yscrollcommand'] = log_scrollbar.set
        
        # 2. Error Logger Tab
        error_log_frame = ttk.Frame(self.notebook, padding="5")
        self.notebook.add(error_log_frame, text="Error Logger")

        self.error_text = tk.Text(error_log_frame, height=10, bd=0, relief="flat", font=('Consolas', 9), state=tk.DISABLED)
        self.error_text.pack(fill="both", expand=True, pady=(0, 10))

        self.copy_errors_button = ttk.Button(error_log_frame, text="Copy All Failed URLs", command=self.copy_failed_urls, style='Accent.TButton')
        self.copy_errors_button.pack(fill='x')
        
    # --- Context Menu Functionality ---
    def create_context_menu(self, event):
        """Creates and displays the standard right-click context menu."""
        widget = event.widget
        
        # 1. Define standard actions
        def copy():
            try:
                widget.event_generate("<<Copy>>")
            except tk.TclError:
                # Handle ttk.Entry copy specifically
                if isinstance(widget, ttk.Entry):
                    selected_text = widget.selection_get()
                    self.master.clipboard_clear()
                    self.master.clipboard_append(selected_text)

        def paste():
            widget.event_generate("<<Paste>>")

        def select_all():
            if isinstance(widget, tk.Text):
                widget.tag_add("sel", "1.0", tk.END)
            elif isinstance(widget, ttk.Entry):
                widget.selection_range(0, tk.END)
                widget.icursor(tk.END) # Place cursor at end

        # 2. Create the menu
        menu = tk.Menu(widget, tearoff=0)
        menu.add_command(label="Copy", command=copy)
        menu.add_command(label="Paste", command=paste)
        menu.add_separator()
        menu.add_command(label="Select All", command=select_all)
        
        # 3. Display the menu at mouse coordinates
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def setup_bindings(self):
        """Sets up validation for option entries and binds right-click for context menu."""
        vcmd_date = (self.master.register(self._validate_int_input), '%P')
        self.date_filter_entry.config(validate='key', validatecommand=vcmd_date)
        self.playlist_start_entry.config(validate='key', validatecommand=vcmd_date)
        self.playlist_end_entry.config(validate='key', validatecommand=vcmd_date)
        
        # Bind context menu to URL Text Area and Output Entry
        self.url_text.bind("<Button-3>", self.create_context_menu)
        self.output_entry.bind("<Button-3>", self.create_context_menu)


    def _validate_int_input(self, P):
        """Validation function to ensure input is empty or contains only digits."""
        return P.isdigit() or P == ""

    def _update_quality_options(self):
        """Updates the quality combobox choices based on the selected download type."""
        selected_type = self.download_type.get()
        current_value = self.quality_var.get()
        
        if selected_type == 'Video':
            new_choices = [c for c in QUALITY_MAP.keys() if c.startswith('video_')]
            if not current_value.startswith('video_'):
                self.quality_var.set('video_best')
        else: # Audio
            new_choices = [c for c in QUALITY_MAP.keys() if c.startswith('audio_')]
            if not current_value.startswith('audio_'):
                self.quality_var.set('audio_mp3')
                
        self.quality_menu.config(values=new_choices)

    def apply_theme(self, mode):
        """Applies the selected light or dark theme to all widgets."""
        # Get the theme name - if theme_menu hasn't been created yet, use 'Nord'
        # Determine selected palette (no mode). Default to 'Nord' if not ready.
        theme_name = self.current_palette.get() if hasattr(self, 'theme_menu') else 'Nord'
        # Build the full theme key using the current mode
        theme_key = f"{theme_name} ({'Dark' if mode == 'dark' else 'Light'})"
        
        # Get the theme colors
        theme = THEMES.get(theme_key, THEMES.get('Nord (Dark)'))
        
        if theme is None:  # Fallback to Nord dark if theme not found
            theme = THEMES.get('Nord (Dark)')
        
        self.master.configure(bg=theme['BG_ROOT'])

        # General TTK Styles
        self.style.configure('TFrame', background=theme['BG_FRAME'])
        self.style.configure('TLabel', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], font=('Inter', 10))
        self.style.configure('Title.TLabel', background=theme['BG_FRAME'], foreground=theme['TITLE_COLOR'], font=('Inter', 18, 'bold'))
        self.style.configure('TRadiobutton', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], selectcolor=theme['BG_FRAME'], font=('Inter', 10))
        self.style.configure('TCheckbutton', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], selectcolor=theme['BG_FRAME'], font=('Inter', 10))
        
        # Notebook (Tab) Styling - Important for modern look
        self.style.configure('TNotebook', background=theme['BG_FRAME'], borderwidth=0)
        self.style.configure('TNotebook.Tab', background=theme['BG_DISABLED'], foreground=theme['FG_TEXT'], padding=[10, 5])
        self.style.map('TNotebook.Tab', background=[('selected', theme['BG_ENTRY'])], foreground=[('selected', theme['FG_TEXT'])])
        
        # Progress Bar Styling (Apply colors to the default TProgressbar)
        self.style.configure('TProgressbar', 
                             background=theme['ACCENT_GREEN'], # Color of the filled part
                             troughcolor=theme['BG_DISABLED'] # Color of the empty part
                            )

        # Standard Buttons
        self.style.configure('Accent.TButton', background=theme['ACCENT_BLUE'], foreground=theme['FG_TEXT'], font=('Inter', 10, 'bold'), borderwidth=0)
        self.style.map('Accent.TButton', background=[('active', theme['TITLE_COLOR']), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])
        self.style.configure('Toggle.TButton', background=theme['ACCENT_BLUE'], foreground=theme['FG_TEXT'], font=('Inter', 10), borderwidth=0)
        self.style.map('Toggle.TButton', background=[('active', theme['TITLE_COLOR'])])

        # Start Button
        self.style.configure('Start.TButton', background=theme['ACCENT_GREEN'], foreground='black', font=('Inter', 12, 'bold'), borderwidth=0)
        self.style.map('Start.TButton', background=[('active', '#B4E19D'), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])
        
        # Stop Button
        self.style.configure('Stop.TButton', background=theme['ACCENT_RED'], foreground='white', font=('Inter', 12, 'bold'), borderwidth=0)
        self.style.map('Stop.TButton', background=[('active', '#E0A3A8'), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])

        # Status Bar
        self.style.configure('Status.TFrame', background=theme['BG_ENTRY'])
        self.style.configure('Status.TLabel', background=theme['BG_ENTRY'], foreground=theme['TITLE_COLOR'], font=('Inter', 10, 'italic'))

        # TEntry (for ttk.Entry and ttk.Combobox) styling 
        self.style.configure('TEntry', 
            fieldbackground=theme['BG_ENTRY'], 
            foreground=theme['FG_TEXT'],
            insertbackground=theme['FG_TEXT'] 
        )
        self.style.map('TEntry', 
            fieldbackground=[('disabled', theme['BG_DISABLED'])],
            foreground=[('disabled', theme['FG_DISABLED'])]
        )

        # Direct widget configuration (for tk.Text inputs)
        for widget in [self.url_text, self.log_text, self.error_text]:
            widget.config(
                bg=theme['BG_ENTRY'], 
                fg=theme['FG_TEXT'], 
                insertbackground=theme['FG_TEXT']
            )
            
        # Update Toggle button emoji
        if mode == 'dark':
            self.toggle_button.config(text="☀️")
        else:
            self.toggle_button.config(text="🌙")
            
    def toggle_theme(self):
        """Switches between light and dark themes while keeping the same theme palette."""
        self.current_mode = 'light' if self.current_mode == 'dark' else 'dark'
        # Keep the palette selection unchanged; re-apply the theme using the new mode
        self.apply_theme(self.current_mode)

    def on_palette_changed(self, event=None):
        """Called when the user selects a new palette from the dropdown.

        The dropdown only changes the palette (e.g. 'Nord'). The light/dark mode
        remains controlled exclusively by the toggle button.
        """
        # Apply the newly selected palette using the current mode
        self.apply_theme(self.current_mode)
        
    def select_output_dir(self):
        """Opens a dialog to select the output directory."""
        directory = filedialog.askdirectory(title="Select Output Folder")
        if directory:
            self.output_dir.set(directory)

    def open_output_folder(self):
        """Opens the output directory in the system's file explorer."""
        output_path = self.output_dir.get()
        if not os.path.isdir(output_path):
            self._update_status(f"Error: Output path not found or not a directory: {output_path}")
            return

        try:
            # Use platform-specific command to open the folder
            if sys.platform == "win32":
                os.startfile(output_path)
            elif sys.platform == "darwin":  # macOS
                subprocess.Popen(["open", output_path])
            else:  # Linux/Unix
                subprocess.Popen(["xdg-open", output_path])
            self._update_status(f"Opened output folder: {output_path}")
        except Exception as e:
            self._update_status(f"Error opening folder: {e}")
            
    def _log(self, message):
        """Thread-safe logging to the Download Log Text widget."""
        self.msg_queue.put(('log', message))

    def _update_status(self, message):
        """Thread-safe status bar update (used for non-download status)."""
        self.msg_queue.put(('status', message))
        
    def _update_status_and_progress(self, status_msg, percentage, mode='determinate'):
        """Thread-safe update for both status text and progress bar."""
        self.msg_queue.put(('progress_update', (status_msg, percentage, mode)))

    def _update_error_log_ui(self):
        """Updates the Error Logger text widget with the list of failed URLs."""
        self.error_text.config(state=tk.NORMAL)
        self.error_text.delete("1.0", tk.END)
        
        if self.failed_urls:
            content = f"--- {len(self.failed_urls)} Failed URLs ---\n\n"
            content += "\n".join(self.failed_urls)
            self.error_text.insert(tk.END, content)
            self.copy_errors_button.config(state=tk.NORMAL)
        else:
            self.error_text.insert(tk.END, "No errors logged yet!")
            self.copy_errors_button.config(state=tk.DISABLED)
            
        self.error_text.config(state=tk.DISABLED)

    def copy_failed_urls(self):
        """Copies the list of failed URLs to the clipboard."""
        if self.failed_urls:
            links = "\n".join(self.failed_urls)
            self.master.clipboard_clear()
            self.master.clipboard_append(links)
            self._update_status(f"Copied {len(self.failed_urls)} failed URLs to clipboard!")
        else:
            self._update_status("No failed URLs to copy.")

    def _update_control_buttons(self):
        """Updates the state and text of the control buttons."""
        if self.is_downloading:
            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.NORMAL)
            self.stop_button.configure(state=tk.NORMAL)
            
            if self.pause_requested.is_set():
                self.pause_button.configure(text="RESUME", style='Start.TButton')
            else:
                self.pause_button.configure(text="PAUSE", style='Accent.TButton')

        else:
            self.start_button.configure(text="START DOWNLOAD", state=tk.NORMAL)
            self.pause_button.configure(text="PAUSE", state=tk.DISABLED, style='Accent.TButton')
            self.stop_button.configure(state=tk.DISABLED)

    def check_queue(self):
        """Checks the queue for messages from the worker thread and updates the UI."""
        while not self.msg_queue.empty():
            try:
                msg_type, content = self.msg_queue.get(0)
                if msg_type == 'log':
                    self.log_text.insert(tk.END, content + "\n")
                    self.log_text.see(tk.END)
                elif msg_type == 'status':
                    self.status_text.set(content)
                    # When a simple status is set (not progress update), assume download finished/stopped
                    if "Ready" in content or "complete" in content or "Terminating" in content:
                        self.progress_bar['value'] = 0
                        self.progress_bar.configure(mode='determinate')
                elif msg_type == 'update_buttons':
                    self._update_control_buttons()
                elif msg_type == 'update_error_log':
                    self._update_error_log_ui()
                elif msg_type == 'progress_update': # Handle status and progress bar updates
                    status_msg, percentage, mode = content
                    self.status_text.set(status_msg)
                    self.progress_bar.configure(mode=mode)
                    if percentage >= 0:
                        self.progress_bar['value'] = percentage
                    else:
                        # Set to 0 if indeterminate or unknown percentage
                        self.progress_bar['value'] = 0 
                
            except Exception:
                pass # Ignore occasional queue issues
        
        self.master.after(100, self.check_queue)
        
    def toggle_pause(self):
        """Toggles the pause state."""
        if self.is_downloading:
            if self.pause_requested.is_set():
                self.pause_requested.clear()
                self._update_status("Download resumed.")
            else:
                self.pause_requested.set()
                self._update_status("Download paused. Hit RESUME to continue.")
            
            self.msg_queue.put(('update_buttons', None)) 
        
    def request_stop(self):
        """Sets the stop flag to terminate the download session."""
        if self.is_downloading:
            self.stop_requested.set()
            if self.pause_requested.is_set():
                self.pause_requested.clear()
            self._update_status("STOP request received. Terminating current download and session...")
            self.stop_button.configure(state=tk.DISABLED)
            
    def start_download_thread(self):
        """
        Initiates the main download process by creating and starting 
        a non-blocking thread, after validating input URLs.
        """
        if self.is_downloading:
            self._log("[WARNING] A download is already in progress.")
            return

        urls_raw = self.url_text.get("1.0", tk.END).strip()
        
        # Split input by line and filter out empty strings
        urls = [u.strip() for u in urls_raw.splitlines() if u.strip()]
        
        if not urls:
            self._update_status("Please paste one or more valid URLs to begin.")
            return

        self._log(f"Starting download session for {len(urls)} URL(s)...")
        
        # Reset error log for the new session
        self.failed_urls = []
        self.msg_queue.put(('update_error_log', None)) 
        
        self.is_downloading = True
        self.stop_requested.clear()
        self.pause_requested.clear()
        self.msg_queue.put(('update_buttons', None)) 
        
        # Create and start the thread, passing the list of URLs to the worker
        self.download_thread = threading.Thread(
            target=self._download_worker, 
            args=(urls,), 
            daemon=True
        )
        self.download_thread.start()

    def _progress_hook(self, d):
        """Custom progress hook adapted for the GUI environment, providing detailed status and progress bar updates."""
        
        # 1. Stop Check
        if self.stop_requested.is_set():
            raise DownloadError("Download session terminated by user.")

        # 2. Pause Check
        while self.pause_requested.is_set():
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
                self._update_status_and_progress(status_msg, percent_int, mode='determinate')
            else:
                 # Fallback for streams/downloads where total size is unknown
                 percent = d.get('_percent_str', 'N/A')
                 speed = d.get('_speed_str', 'N/A')
                 eta = d.get('_eta_str', 'N/A')
                 status_msg = f"Downloading: '{display_title}' - {percent} at {speed} ETA: {eta}"
                 self._update_status_and_progress(status_msg, 0, mode='indeterminate')
                 
        elif d['status'] == 'postprocessing':
            status_msg = f"Post-processing: '{display_title}' (Merging/Converting...)"
            # Use indeterminate mode for post-processing as percentage is usually unavailable
            self._update_status_and_progress(status_msg, 0, mode='indeterminate')
            
        elif d['status'] == 'finished':
            filename = d.get('filename', 'Unknown File')
            self._log(f"  >> FINISHED: {os.path.basename(filename)}")
            self._update_status_and_progress(f"Merge/Conversion complete for {os.path.basename(filename)}", 100, mode='determinate')
        
        elif d['status'] == 'error':
            self._log(f"  >> ERROR: {d.get('error', 'Unknown Error')}")

    def _download_worker(self, urls):
        """The function run in the separate thread to handle yt-dlp downloads."""
        
        try:
            output_dir = self.output_dir.get()
            quality_key = self.quality_var.get()
            download_type = self.download_type.get()
            
            format_string = QUALITY_MAP.get(quality_key, QUALITY_MAP['video_best'])
            
            # 1. Create directory if needed
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                self._log(f"Created output directory: {output_dir}")

            self._log(f"Download Type: {download_type} | Format: {quality_key} (String: {format_string})")
            
            ydl_opts = {
                'format': format_string,
                'outtmpl': os.path.join(output_dir, '%(title)s - %(uploader)s - %(id)s.%(ext)s'),
                'restrictfilenames': True,
                'noplaylist': False, 
                'progress_hooks': [self._progress_hook],
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
            days_str = self.date_filter_days.get().strip()
            if days_str and days_str.isdigit():
                days = int(days_str)
                cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
                ydl_opts['dateafter'] = cutoff_date
                self._log(f"Filtering: Skipping media uploaded before {cutoff_date} ({days} days ago).")

            # 4. Configure Playlist/Index Filters
            start_index_str = self.playlist_start_var.get().strip()
            end_index_str = self.playlist_end_var.get().strip()

            if start_index_str and start_index_str.isdigit() and int(start_index_str) > 0:
                ydl_opts['playlist_start'] = int(start_index_str)
                self._log(f"Collection: Starting download from index {start_index_str}.")
            
            if end_index_str and end_index_str.isdigit():
                ydl_opts['playlist_end'] = int(end_index_str)
                self._log(f"Collection: Ending download at index {end_index_str}.")

            # 5. Configure Skip Shorts
            if self.skip_shorts_var.get():
                ydl_opts['match_filter'] = lambda info, incomplete: None if 'shorts/' in info['webpage_url'] else None
                self._log("Filtering: Attempting to skip short-form media.")

            # --- Execute Download ---
            
            for i, url in enumerate(urls):
                if self.stop_requested.is_set():
                    self._log("\n[SESSION TERMINATED] Stop flag detected. Halting further URL processing.")
                    break
                    
                self._log(f"\n[{i+1}/{len(urls)}] Processing URL: {url}")
                # Reset progress bar to 0 before a new item starts
                self._update_status_and_progress(f"Starting analysis for URL {i+1}...", 0, 'indeterminate')
                
                while self.pause_requested.is_set():
                    self._update_status(f"PAUSED before processing URL {i+1}. Hit RESUME to continue.")
                    time.sleep(0.5)

                try:
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                except DownloadError as e:
                    # Specific error handling for yt-dlp DownloadErrors
                    if "Download session terminated by user" in str(e):
                         self._log(f"\n[SESSION TERMINATED] User stopped download {i+1}.")
                         self.stop_requested.set()
                         break
                    else:
                        error_msg = str(e).splitlines()[0]
                        self._log(f"[ERROR] Failed to download: {url}. The link may be private or incorrect. Error: {error_msg}")
                        self.failed_urls.append(url)
                except Exception as e:
                    # Catch all other unexpected errors
                    self._log(f"[FATAL] An unexpected error occurred for {url}: {e}")
                    self.failed_urls.append(url)

        except Exception as e:
            self._log(f"Fatal error during download process: {e}")
            
        finally:
            if self.stop_requested.is_set():
                 final_message = "\n--- Download Session TERMINATED by user. ---"
            else:
                 final_message = "\n--- All Downloads Finished! ---"
            
            self.msg_queue.put(('log', final_message))
            self.msg_queue.put(('update_error_log', None)) # CRITICAL: Update error log
            
            # Reset status and progress bar
            self._update_status_and_progress("Download session complete. Ready.", 0, 'determinate')
            
            # Reset final state
            self.is_downloading = False
            self.stop_requested.clear()
            self.pause_requested.clear()
            self.msg_queue.put(('update_buttons', None)) 


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
