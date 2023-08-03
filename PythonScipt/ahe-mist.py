import os
import cv2

def apply_ahe(input_image_path, output_image_path, tile_size=8):
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
            
            # Apply AHE to the grayscale image
            clahe = cv2.createCLAHE(tileGridSize=(tile_size, tile_size))
            equalized = clahe.apply(gray)
            
            # Save the enhanced image
            output_path = os.path.join(output_image_path, file)
            cv2.imwrite(output_path, equalized)
            
            print(f"Enhanced image saved: {output_path}")

# Specify input and output directories
input_image_path = 'C:\\Users\\Full Scale\\Documents\\MSIT\\PythonScipt\\blur-output-img'
output_image_path = 'C:\\Users\\Full Scale\\Documents\MSIT\\PythonScipt\\ahe-output-img'

# Specify AHE parameter (tile_size)
tile_size = 8

# Apply AHE to all images in the input directory
apply_ahe(input_image_path, output_image_path, tile_size)
