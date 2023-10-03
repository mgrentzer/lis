import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Load the shapefile
shapefile = gpd.read_file('ky_layers/globalwatershed.shp')

# Open the georeferenced GIF image
with rasterio.open('example.tiff') as src:
    # Read the raster data
    raster_data = src.read(1)  # You may need to specify the band number

    # Get the affine transform for the raster
    transform = src.transform

    # Clip the raster to the shapefile's geometry
    clipped_raster, clipped_transform = mask(src, shapefile.geometry, crop=True)

# Define the output file path
output_path = 'output_clipped_raster.tiff'

# Write the clipped raster to a new GeoTIFF file
with rasterio.open(output_path, 'w', driver='GTiff', height=clipped_raster.shape[1], width=clipped_raster.shape[2], count=clipped_raster.shape[0],  # Use the number of bands from clipped_raster
                dtype=str(clipped_raster.dtype), crs=src.crs, transform=clipped_transform) as dst:
    dst.write(clipped_raster)

