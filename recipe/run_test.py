import reference
from affine import Affine
from rasterstats import zonal_stats
import numpy as np
from shapely.geometry import Polygon

griddelta = 0.01
GRIDWEST = -139.2
GRIDEAST = -55.1
GRIDNORTH = 54.51
GRIDSOUTH = 19.47
PRECIP_AFF = Affine(0.01, 0., GRIDWEST, 0., -0.01, GRIDNORTH)
YSZ = (GRIDNORTH - GRIDSOUTH) / 0.01
XSZ = (GRIDEAST - GRIDWEST) / 0.01

ones = np.ones((int(YSZ), int(XSZ)))
counts = np.zeros((int(YSZ), int(XSZ)))
lons = np.arange(GRIDWEST, GRIDEAST, griddelta)
lats = np.arange(GRIDSOUTH, GRIDNORTH, griddelta)

p = Polygon([[-104.92, 34.14],[-105.28, 34.13],[-105.34, 33.55],[-104.89, 33.55],[-104.92, 34.14]])

zs = zonal_stats(p, ones, affine=PRECIP_AFF, nodata=-1,
                 all_touched=True, raster_out=True)
