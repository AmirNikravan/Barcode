from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the input image
    with Image.open(input_path) as img:
        # Resize the image using LANCZOS filter for high-quality downsampling
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        # Save the resized image to the output path
        resized_img.save(output_path)
        print(f"Image saved to {output_path}")

if __name__ == "__main__":
    # Define the input and output image paths
    input_image_path = "/home/nullptr/programming/barcode/Barcode/images/123.jpeg"  # Replace with your input image path
    output_image_path = "output.jpg"  # Replace with your desired output image path

    # Define the new resolution
    new_width = 100  # Replace with the desired width
    new_height = 50  # Replace with the desired height

    # Resize the image
    resize_image(input_image_path, output_image_path, new_width, new_height)
