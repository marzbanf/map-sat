from socket import INADDR_ANY
import geopandas as gpd
import os
from shapefile_utils import get_largest_geometry

ROOT = os.getcwd()
COUNTRIES = f'{ROOT}/kermanshah_data/kermanshah_region.shp'
KERMANSHAH_FULL = f'{ROOT}/kermanshah_data/kermanshah_full.shp'
KERMANSHAH = f'{ROOT}/kermanshah_data/kermanshah.shp'
EPSG = "EPSG:4326"

# Countries Iran
gdf_country = gpd.read_file(COUNTRIES)
# Filter only for SCT
coastline_sct = gdf_country[gdf_country.NAME=='Kermanshah']
# Save Kermanshah boundaries as shapefile
coastline_sct.to_file(KERMANSHAH_FULL, driver='ESRI Shapefile')
print("Kermanshah shapefile (full, with kermanshah) saved")

# Read the shapefile for Kermanshah (full, mainland + kermanshah)
kermanshah_shapefile = gpd.read_file(KERMANSHAH_FULL)
# Get the largest geometry from the kermanshah shapefile (thus, the mainland)
# And convert it to CRS common format
sct_kermanshah = get_largest_geometry(kermanshah_shapefile).to_crs(EPSG)
sct_kermanshah.to_file(KERMANSHAH, driver='ESRI Shapefile')
print("Kermanshah shapefile (mainland only) saved")