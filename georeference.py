import rasterio
from rasterio.control import GroundControlPoint
from rasterio.transform import from_gcps


gcps = [
    GroundControlPoint(row=480.5, col=67.5, x=-92.0, y=36.0),
    GroundControlPoint(row=291.5, col=825.5, x=-82.0, y=38.0),
    GroundControlPoint(row=291.5, col=522.5, x= -86.0, y=38.0)
]

transform = from_gcps(gcps)
crs = 'epsg:3857'

with rasterio.open('example.tiff', 'r+') as dst:
        dst.crs = crs
        dst.transform = transform

