import rasterio
from rasterio.control import GroundControlPoint
from rasterio.transform import Affine

gcps = [
    GroundControlPoint(row=100, col=200, x=-122.0, y=45.0),
    GroundControlPoint(row=150, col=250, x=-121.5, y=45.2),
    # Add more GCPs as needed
]