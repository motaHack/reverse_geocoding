import csv
import configparser
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

    reslist = [str(lon),
               str(lat),
               geos['N03_001'].to_string(index=False),
               geos['N03_002'].to_string(index=False),
               geos['N03_003'].to_string(index=False),
               geos['N03_004'].to_string(index=False),
               geos['N03_007'].to_string(index=False)]

    return(reslist)

# read config.ini
inifile = configparser.ConfigParser()
inifile.read('config.ini', 'UTF-8')
shpfile = inifile.get('file','shp')
inputfile = inifile.get('file','input')
outputfile = inifile.get('file','output')
column_no_lat = int(inifile.get('column','latitude'))
column_no_lon = int(inifile.get('column','longitude'))

# main
shdf = gpd.read_file(shpfile)
output = open(outputfile, 'w')
writer = csv.writer(output)

with open(inputfile) as f:
  reader = csv.reader(f)
  next(reader)
  for row in reader:
    longitude = float(row[column_no_lon])
    latitude = float(row[column_no_lat])
    reslist = reverse_geo(shdf, longitude, latitude)
    writer.writerow(reslist)

output.close()
