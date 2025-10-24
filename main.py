# main.py

import tkinter as tk
from app_ui import ImageViewerApp  # Import your new UI class

def main():
    """Main function to initialize and run the application."""
    
    # 1. Create the root window
    window = tk.Tk()
    
    # 2. Create an instance of your app class
    #    This one line builds the entire UI
    app = ImageViewerApp(window)
    
    # 3. Start the main event loop
    window.mainloop()


if __name__ == "__main__":
    main()