# make feather file from shpfile
import sys
import geopandas as gpd
from geofeather import *
from geopandas.geoseries import *

print('start!')
args = sys.argv
shpfile = args[1]
feather_file = shpfile.replace('shp', 'feather')
shdf = gpd.read_file(shpfile, encoding='SHIFT-JIS')
to_geofeather(shdf, feather_file)
print('done!')
