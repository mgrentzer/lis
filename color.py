import rasterio
import numpy as np
from PIL import Image

# Input GIF file path
gif_file_path = 'example.gif'

# Output TIFF file path
tiff_file_path = 'example.tiff'

# Open the GIF file using Pillow (PIL) to extract the individual frames
with Image.open(gif_file_path) as img:
    frames = [frame.convert('RGB') for frame in img.split()]

# Create a new TIFF file using Rasterio
with rasterio.open(
    tiff_file_path,
    'w',
    driver='GTiff',
    width=frames[0].width,
    height=frames[0].height,
    count=3,  # Number of color bands (R, G, B)
    dtype='uint8'  # Data type for each band
) as dst:
    for i, frame in enumerate(frames):
        # Convert each frame to a NumPy array
        frame_array = np.array(frame)

        # Separate the RGB channels into individual bands
        red_band = frame_array[:, :, 0]
        green_band = frame_array[:, :, 1]
        blue_band = frame_array[:, :, 2]

        # Write each band to the TIFF file
        dst.write(red_band, 1)   # Red band
        dst.write(green_band, 2) # Green band
        dst.write(blue_band, 3)  # Blue band

print(f'TIFF file saved at {tiff_file_path}')
