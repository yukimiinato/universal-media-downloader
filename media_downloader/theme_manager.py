"""
Theme management for the Media Downloader application.
Handles theme application, palette switching, and light/dark mode toggling.
"""

import tkinter as tk
from themes import THEMES, get_all_theme_names


def apply_theme(app, mode):
    """Applies the selected light or dark theme to all widgets."""
    # Get the theme name - if theme_menu hasn't been created yet, use 'Nord'
    # Determine selected palette (no mode). Default to 'Nord' if not ready.
    theme_name = app.current_palette.get() if hasattr(app, 'theme_menu') else 'Nord'
    # Build the full theme key using the current mode
    theme_key = f"{theme_name} ({'Dark' if mode == 'dark' else 'Light'})"
    
    # Get the theme colors
    theme = THEMES.get(theme_key, THEMES.get('Nord (Dark)'))
    
    if theme is None:  # Fallback to Nord dark if theme not found
        theme = THEMES.get('Nord (Dark)')
    
    app.master.configure(bg=theme['BG_ROOT'])

    # General TTK Styles
    app.style.configure('TFrame', background=theme['BG_FRAME'])
    app.style.configure('TLabel', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], font=('Segoe UI', 11))
    app.style.configure('Title.TLabel', background=theme['BG_FRAME'], foreground=theme['TITLE_COLOR'], font=('Segoe UI', 22, 'bold'))
    app.style.configure('TRadiobutton', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], selectcolor=theme['BG_FRAME'], font=('Segoe UI', 11))
    app.style.configure('TCheckbutton', background=theme['BG_FRAME'], foreground=theme['FG_TEXT'], selectcolor=theme['BG_FRAME'], font=('Segoe UI', 11))
    
    # Notebook (Tab) Styling - Important for modern look
    app.style.configure('TNotebook', background=theme['BG_FRAME'], borderwidth=0)
    app.style.configure('TNotebook.Tab', background=theme['BG_DISABLED'], foreground=theme['FG_TEXT'], padding=[10, 5])
    app.style.map('TNotebook.Tab', background=[('selected', theme['BG_ENTRY'])], foreground=[('selected', theme['FG_TEXT'])])
    
    # Progress Bar Styling (Apply colors to the default TProgressbar)
    app.style.configure('TProgressbar', 
                         background=theme['ACCENT_GREEN'], # Color of the filled part
                         troughcolor=theme['BG_DISABLED'] # Color of the empty part
                        )

    # Standard Buttons
    app.style.configure('Accent.TButton', background=theme['ACCENT_BLUE'], foreground=theme['FG_TEXT'], font=('Segoe UI', 11, 'bold'), borderwidth=0)
    app.style.map('Accent.TButton', background=[('active', theme['TITLE_COLOR']), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])
    app.style.configure('Toggle.TButton', background=theme['ACCENT_BLUE'], foreground=theme['FG_TEXT'], font=('Segoe UI', 11), borderwidth=0)
    app.style.map('Toggle.TButton', background=[('active', theme['TITLE_COLOR'])])

    # Start Button
    app.style.configure('Start.TButton', background=theme['ACCENT_GREEN'], foreground='black', font=('Segoe UI', 13, 'bold'), borderwidth=0)
    app.style.map('Start.TButton', background=[('active', '#B4E19D'), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])
    
    # Stop Button
    app.style.configure('Stop.TButton', background=theme['ACCENT_RED'], foreground='white', font=('Segoe UI', 13, 'bold'), borderwidth=0)
    app.style.map('Stop.TButton', background=[('active', '#E0A3A8'), ('disabled', theme['BG_DISABLED'])], foreground=[('disabled', theme['FG_DISABLED'])])

    # Status Bar
    app.style.configure('Status.TFrame', background=theme['BG_ENTRY'])
    app.style.configure('Status.TLabel', background=theme['BG_ENTRY'], foreground=theme['TITLE_COLOR'], font=('Segoe UI', 11, 'italic'))

    # TEntry (for ttk.Entry and ttk.Combobox) styling 
    app.style.configure('TEntry', 
        fieldbackground=theme['BG_ENTRY'], 
        foreground=theme['FG_TEXT'],
        insertbackground=theme['FG_TEXT'] 
    )
    app.style.map('TEntry', 
        fieldbackground=[('disabled', theme['BG_DISABLED'])],
        foreground=[('disabled', theme['FG_DISABLED'])]
    )

    # Direct widget configuration (for tk.Text inputs)
    for widget in [app.url_text, app.log_text, app.error_text]:
        widget.config(
            bg=theme['BG_ENTRY'], 
            fg=theme['FG_TEXT'], 
            insertbackground=theme['FG_TEXT']
        )
        
    # Update Toggle button emoji
    if mode == 'dark':
        app.toggle_button.config(text="☀️")
    else:
        app.toggle_button.config(text="🌙")


def toggle_theme(app):
    """Switches between light and dark themes while keeping the same theme palette."""
    app.current_mode = 'light' if app.current_mode == 'dark' else 'dark'
    # Keep the palette selection unchanged; re-apply the theme using the new mode
    apply_theme(app, app.current_mode)


def on_palette_changed(app, event=None):
    """Called when the user selects a new palette from the dropdown.

    The dropdown only changes the palette (e.g. 'Nord'). The light/dark mode
    remains controlled exclusively by the toggle button.
    """
    # Apply the newly selected palette using the current mode
    apply_theme(app, app.current_mode)
