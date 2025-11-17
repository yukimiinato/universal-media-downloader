# Universal Media Downloader v1.0.1

A beautiful, feature-rich GUI application for downloading videos and audio from YouTube and other supported platforms.

## Features

### 🎬 Download Options
- **Video Quality**: Best, 1080p, 720p, 480p
- **Audio Formats**: MP3, Opus
- **Batch Downloads**: Multiple URLs at once
- **Playlist Support**: Download entire playlists with start/end index control

### 🎨 Themes & Customization
- **80 Beautiful Themes** (40 unique palettes with light/dark variants)
- Popular themes: Nord, Dracula, Monokai, Tokyonight, Gruvbox, Solarized, and more
- Real-time theme switching with light/dark mode toggle
- Enhanced contrast for better visibility

### 🛠️ Advanced Features
- **Smart Filters**:
  - Skip media older than X days
  - Skip short-form content (TikTok, YouTube Shorts)
  - Playlist range selection
- **Download Control**: Start, Pause, Resume, Stop buttons
- **Real-time Monitoring**:
  - Progress bar with speed and ETA
  - Download log with detailed information
  - Error log with failed URL tracking
- **Quick Actions**:
  - Open output folder directly
  - Copy all failed URLs to clipboard

## System Requirements

### Python
- Python 3.8 or newer
- tkinter (usually included with Python)

### External Tools
- **yt-dlp**: Media download library (auto-installed on first run)
- **FFmpeg**: Video/audio processing (auto-installed on first run)
  - Windows: Auto-install via Winget
  - Linux: Auto-install via apt (Debian/Ubuntu) or dnf (Fedora/RHEL)
  - macOS: Auto-install via Homebrew

### Platform Support
- ✅ Windows (auto-install for all dependencies)
- ✅ Linux (auto-install for all dependencies)
- ✅ macOS (auto-install for all dependencies)

## Installation

### Windows

1. **Clone the repository** (using Git or download as ZIP)
   ```cmd
   git clone https://github.com/yourusername/universal-media-downloader.git
   cd universal-media-downloader
   ```

2. **Run the application**
   ```cmd
   python run_downloader.py
   ```

3. **First Run**: The application will automatically:
   - Install yt-dlp (Python dependency)
   - Install FFmpeg via Winget (system dependency)
   - Then launch the GUI

### Linux (Debian/Ubuntu)

1. **Install Python and dependencies** (if not already installed)
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk git
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/universal-media-downloader.git
   cd universal-media-downloader
   ```

3. **Run the application**
   ```bash
   python3 run_downloader.py
   ```

4. **First Run**: The application will automatically:
   - Install yt-dlp (Python dependency)
   - Install FFmpeg via apt (system dependency)
   - Then launch the GUI

### Linux (Fedora/RHEL)

1. **Install Python and dependencies** (if not already installed)
   ```bash
   sudo dnf install python3 python3-pip python3-tkinter git
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/universal-media-downloader.git
   cd universal-media-downloader
   ```

3. **Run the application**
   ```bash
   python3 run_downloader.py
   ```

4. **First Run**: The application will automatically:
   - Install yt-dlp (Python dependency)
   - Install FFmpeg via dnf (system dependency)
   - Then launch the GUI

### Linux (Arch)

1. **Install Python and dependencies** (if not already installed)
   ```bash
   sudo pacman -S python python-pip tk git
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/universal-media-downloader.git
   cd universal-media-downloader
   ```

3. **Run the application**
   ```bash
   python run_downloader.py
   ```

4. **First Run**: The application will automatically:
   - Install yt-dlp (Python dependency)
   - Install FFmpeg via pacman (system dependency)
   - Then launch the GUI

### macOS

1. **Install Homebrew** (if not already installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python** (if not already installed)
   ```bash
   brew install python@3.11
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/universal-media-downloader.git
   cd universal-media-downloader
   ```

4. **Run the application**
   ```bash
   python3 run_downloader.py
   ```

5. **First Run**: The application will automatically:
   - Install yt-dlp (Python dependency)
   - Install FFmpeg via Homebrew (system dependency)
   - Then launch the GUI

## Usage

### Quick Start
```bash
python run_downloader.py
```

### Running from Package Directory
```bash
cd media_downloader
python main.py
```

### Basic Workflow
1. Paste one or more URLs into the input area
2. Select download type (Video or Audio)
3. Choose quality/format
4. Configure optional filters (age, shorts, playlist range)
5. Select output folder
6. Click "START DOWNLOAD"

## Project Structure

```
universal-media-downloader/
├── run_downloader.py           # Main entry point
├── media_downloader/
│   ├── __init__.py             # Package initialization
│   ├── main.py                 # Main application (GUI & download logic)
│   └── themes.py               # 80 themes with improved contrast
├── RUNNING.md                  # Detailed running instructions
└── README.md                   # This file
```

## Themes Included

**Classic Themes**: Nord, Dracula, Monokai, One Dark, Atom One Dark, Gruvbox Dark, Solarized Dark

**Modern Themes**: Tokyonight, Material Darker, Zenburn, Synthwave

**Nature Themes**: Forest, Ocean, Mint, Emerald, Peacock, Sage

**Warm Themes**: Sunset, Sunset Blaze, Sunset Pink, Honey, Marigold, Warm Spice, Coral

**Professional Themes**: Steel, Storm, Midnight, Arctic, Cyber

**Color Palettes**: Lavender, Rose, Ruby, Grape, Aubergine, Amethyst, Forest Fire

**And 10 more!** Each theme includes both light and dark variants.

## Keyboard & Mouse Features

- **Right-click Context Menu**: Copy, Paste, Select All in text fields
- **Light/Dark Mode**: Quick toggle with emoji button (☀️/🌙)
- **Theme Dropdown**: 80 themes to choose from

## Dependencies

### Core Dependencies
- tkinter (included with Python)
- yt-dlp (auto-installed)

### Optional but Recommended
- FFmpeg (auto-installable on Windows)

Install dependencies manually:
```bash
pip install yt-dlp
```

## Troubleshooting

### Automatic Installation Doesn't Work
If the automatic dependency installation fails for some reason, you can install manually:

**yt-dlp:**
```bash
pip install --upgrade yt-dlp
```

**FFmpeg:**
- **Windows**: Download from https://ffmpeg.org/download.html
- **Linux (Debian/Ubuntu)**: `sudo apt update && sudo apt install ffmpeg`
- **Linux (Fedora/RHEL)**: `sudo dnf install ffmpeg`
- **Linux (Arch)**: `sudo pacman -S ffmpeg`
- **macOS**: `brew install ffmpeg`

### sudo Password Required (Linux)
When installing FFmpeg on Linux, you may be prompted for your sudo password. This is normal and required for system-level package installation.

### tkinter Not Available
- **Windows/macOS**: Usually pre-installed
- **Linux**: `sudo apt-get install python3-tk`

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve themes
- Enhance documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for downloading media you have permission to download. Always respect copyright and terms of service.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for content creators and media enthusiasts**
