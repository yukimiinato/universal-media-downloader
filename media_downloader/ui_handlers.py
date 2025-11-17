"""
UI event handlers for the Media Downloader application.
Manages context menus, bindings, input validation, and file dialogs.
"""

import tkinter as tk
from tkinter import ttk, filedialog
import sys
import os
import subprocess


def create_context_menu(app, event):
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
                app.master.clipboard_clear()
                app.master.clipboard_append(selected_text)

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


def setup_bindings(app):
    """Sets up validation for option entries and binds right-click for context menu."""
    vcmd_date = (app.master.register(validate_int_input), '%P')
    app.date_filter_entry.config(validate='key', validatecommand=vcmd_date)
    app.playlist_start_entry.config(validate='key', validatecommand=vcmd_date)
    app.playlist_end_entry.config(validate='key', validatecommand=vcmd_date)
    
    # Bind context menu to URL Text Area and Output Entry
    app.url_text.bind("<Button-3>", lambda event: create_context_menu(app, event))
    app.output_entry.bind("<Button-3>", lambda event: create_context_menu(app, event))


def validate_int_input(P):
    """Validates that input is an integer or empty string."""
    return P == "" or P.isdigit()


def select_output_dir(app):
    """Opens a dialog to select the output directory."""
    directory = filedialog.askdirectory(title="Select Output Folder")
    if directory:
        app.output_dir.set(directory)


def open_output_folder(app):
    """Opens the output directory in the system's file explorer."""
    output_path = app.output_dir.get()
    if not os.path.isdir(output_path):
        app._update_status(f"Error: Output path not found or not a directory: {output_path}")
        return

    try:
        # Use platform-specific command to open the folder
        if sys.platform == "win32":
            os.startfile(output_path)
        elif sys.platform == "darwin":  # macOS
            subprocess.Popen(["open", output_path])
        else:  # Linux/Unix
            subprocess.Popen(["xdg-open", output_path])
        app._update_status(f"Opened output folder: {output_path}")
    except Exception as e:
        app._update_status(f"Error opening folder: {e}")
