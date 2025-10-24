"""
app_ui.py
~~~~~~~~~

Main user interface for the Random Image Viewer application.

This module provides the ImageViewerApp class which encapsulates
the tkinter UI: a fixed-width control panel (left) and a flexible
image display area (right). The UI is intentionally simple so it
can be embedded in a larger program or run directly from a small
launcher script.

Dependencies:
 - tkinter (standard library)
 - Pillow (PIL) for image loading and resizing

Typical usage (from a launcher module):

    import tkinter as tk
    from app_ui import ImageViewerApp

    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()

"""

from typing import Optional

import tkinter as tk
from PIL import Image, ImageTk
from randomImageSellector2 import random_image_selector2


class ImageViewerApp:
    """A small, single-window image viewer application.

    Responsibilities:
    - Build the main tkinter window and layout
    - Provide a button to load a random image
    - Display the selected image in a right-hand panel

    Notes:
    - The left panel width is fixed (400px) using pack_propagate(False)
      so the control column remains constant while the right panel
      expands to fill the remaining space.
    - Images are resized to 800x500 for consistent display; you can
      change that later or compute dynamic sizes based on the window.
    """

    def __init__(self, master: tk.Tk) -> None:
        """Create and configure the main window and widgets.

        Args:
            master: root tkinter window (tk.Tk).
        """
        self.master = master

        # Basic window configuration
        self.master.title("Random Image Viewer")
        self.master.geometry("1920x1080")
        self.master.config(bg="yellow")

        # Build the UI
        self._create_frames()
        self._create_widgets()

        # Populate the UI with an initial image
        self.on_button_click()

    def _create_frames(self) -> None:
        """Create left (controls) and right (image) frames.

        The left frame is given a fixed width and propagation is
        disabled so it keeps that width regardless of its children's
        natural sizes.
        """

        # Left frame: fixed-width control column
        self.left_frame = tk.Frame(self.master, width=400, bg="pink")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.left_frame.pack_propagate(False)  # keep width=400

        # Right frame: expandable image display
        self.right_frame = tk.Frame(self.master, bg="light blue")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def _create_widgets(self) -> None:
        """Create and place UI widgets inside the frames.

        Widgets that need to be accessed later (like the image label)
        are stored as instance attributes (prefixed with self.).
        """

        # Title in left panel
        greeting_label = tk.Label(
            self.left_frame,
            text="Random Photo Selector",
            bg="#EEBFD8",
            font=("Arial", 40),
            wraplength=350,
            justify=tk.LEFT,
        )
        greeting_label.pack(pady=30, padx=10)

        # Button to fetch and display a random image
        click_me_button = tk.Button(
            self.left_frame,
            text="Get Random Image",
            font=("Arial", 16),
            command=self.on_button_click,
            bg="#007bff",
            fg="#ffffff",
            activebackground="#0056b3",
            activeforeground="#ffffff",
            relief=tk.RAISED,
            borderwidth=2,
            pady=10,
        )
        click_me_button.pack(pady=20, fill=tk.X, padx=10)

        # Image display label in right panel; save as attribute so it
        # can be updated later from on_button_click().
        self.image_label = tk.Label(self.right_frame, borderwidth=20, bg="light blue")
        self.image_label.pack(expand=True)

    def on_button_click(self) -> None:
        """Load a random image and display it in the right-hand panel.

        The function asks the image selector for a path, opens the file
        with Pillow, resizes it for consistent presentation, converts
        it to a PhotoImage, and sets it on the label.
        """
        image_path: Optional[str] = random_image_selector2()

        if not image_path:
            # No images found: show a helpful message in the image area
            self.image_label.config(image=None, text="No images found in folder.")
            return

        try:
            img = Image.open(image_path)
            img = img.resize((1000, 500), Image.Resampling.LANCZOS)

            photo_image = ImageTk.PhotoImage(img)

            # Update the label to show the image
            self.image_label.config(image=photo_image)

            # Keep a reference to the PhotoImage to avoid garbage collection
            self.image_label.image = photo_image

        except Exception as exc:  # catch broad errors from PIL / IO
            print(f"Error loading image {image_path}: {exc}")
            self.image_label.config(image=None, text="Error loading image.")
