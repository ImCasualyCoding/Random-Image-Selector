import os
import random

def random_image_selector2():
    """
    Selects a random image file from a specified folder.
    
    This function looks for image files with common extensions (.jpg, .jpeg, .png, .gif, .bmp)
    in the images folder and returns the full path to a randomly selected image.
    
    Returns:
        str or None: Full path to the randomly selected image file, or None if no images are found.
    """
    # Path to the folder containing images
    image_folder = r"enter your image folder"
    
    # Tuple of supported image file extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    
    # Create a list of all valid image files in the folder
    all_files = [
        files for files in os.listdir(image_folder)
        if files.lower().endswith(valid_extensions)
    ]
    
    # Check if any valid image files were found
    if not all_files:
        print("No image files found in the specified folder.")
        return None
    
    # Select a random image file and return its full path
    random_image_file = random.choice(all_files)
    full_path = os.path.join(image_folder, random_image_file)
    
    return full_path
    


