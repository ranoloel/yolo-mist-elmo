import os
import cv2

def apply_clahe(input_image_path, output_image_path, clip_limit=2.0, tile_size=8):
    # Create output directory if it doesn't exist
    os.makedirs(output_image_path, exist_ok=True)
    
    # Get a list of all files in the input directory
    files = os.listdir(input_image_path)
    
    for file in files:
        # Check if the file is an image
        if file.endswith(('.jpg', 'JPG', '.jpeg', '.png', '.bmp')):
            # Read the input image
            image_path = os.path.join(input_image_path, file)
            image = cv2.imread(image_path)
            
            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Create a CLAHE object
            clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
            
            # Apply CLAHE to the grayscale image
            equalized = clahe.apply(gray)
            
            # Save the enhanced image
            output_path = os.path.join(output_image_path, file)
            cv2.imwrite(output_path, equalized)
            
            print(f"Enhanced image saved: {output_path}")

# Specify input and output directories

input_image_path = 'C:\\Users\\Full Scale\\Documents\\MSIT\\PythonScipt\\final-sample-image'
output_image_path = 'C:\\Users\\Full Scale\\Documents\MSIT\\PythonScipt\\clahe-output-img'

# Specify CLAHE parameters (clip_limit and tile_size)
clip_limit = 2.0
tile_size = 8

# Apply CLAHE to all images in the input directory
apply_clahe(input_image_path, output_image_path, clip_limit, tile_size)
