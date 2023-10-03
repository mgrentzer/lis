


from PIL import Image

def count_pixels_with_rgb_value(image_path, target_rgb):
    # Open the TIFF image
    image = Image.open("output_clipped_raster.tiff")

    # Ensure the image is in RGB mode (some TIFF images may have different modes)
    image = image.convert('RGB')

    # Initialize a count variable
    pixel_count = 0

    # Iterate through each pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            # Get the RGB value of the current pixel
            pixel_rgb = image.getpixel((x, y))

            # Check if the current pixel's RGB value matches the target RGB value
            if pixel_rgb == target_rgb:
                pixel_count += 1

    return pixel_count

# Specify the path to your TIFF image and the target RGB value
image_path = "your_image.tif"
target_rgb = (255, 232, 120)  # Replace R, G, B with your specific RGB values

# Call the function to count pixels with the target RGB value
count = count_pixels_with_rgb_value(image_path, target_rgb)

print(f"Number of pixels with RGB {target_rgb}: {count}")
