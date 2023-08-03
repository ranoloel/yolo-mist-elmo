import os
from PIL import Image, ImageFilter

def blur_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".jpeg", ".png", ".bmp"))]

    for image_file in image_files:
        # Load the image from the input folder
        input_image_path = os.path.join(input_folder, image_file)
        image = Image.open(input_image_path)

        # Apply the blur using the GaussianBlur filter from Pillow
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=3))

        # Save the blurred image to the output folder
        output_image_path = os.path.join(output_folder, image_file)
        blurred_image.save(output_image_path)

if __name__ == "__main__":
    input_folder = 'C:\\Users\\Full Scale\\Documents\\MSIT\\PythonScipt\\final-sample-image'
    output_folder = 'C:\\Users\\Full Scale\\Documents\MSIT\\PythonScipt\\blur-output-img'
    blur_images(input_folder, output_folder)
