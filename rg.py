import csv
import geopandas as gpd
from geopandas.geoseries import *
from shapely.geometry import Point

def reverse_geo(shdf, lon, lat):
    polygon = shdf['geometry']
    point = Point(lon, lat)

    whichtrue = polygon.contains(point)
    row = whichtrue[whichtrue == True].index
    
    geos = shdf.iloc[row]

    if geos.empty == True:
        return(None)

    reslist = [geos['N03_001'].to_string(index=False),
               geos['N03_002'].to_string(index=False),
               geos['N03_003'].to_string(index=False),
               geos['N03_004'].to_string(index=False),
               geos['N03_007'].to_string(index=False)]

    res = ','.join(reslist)

    print(res)


shdf = gpd.read_file('N03-19_190101.shp')

with open('localgovjp-utf8.csv') as f:
  reader = csv.reader(f)
  next(reader)
  for row in reader:
    longitude = float(row[6])
    latitude = float(row[5])
    reverse_geo(shdf, longitude, latitude)
