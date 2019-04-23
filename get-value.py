'''
get-value

this script, when given a csv with latitude and longitude
will return the same csv but with the values of an included raster
file appended to the end
'''
from osgeo import gdal
import logging
import argparse
import csv

logging.basicConfig(level=logging.INFO)

DEFAULT_BAND = 1

parser = argparse.ArgumentParser()
parser.add_argument('--input-csv', help='input csv file',
  required=True)
parser.add_argument('--output-csv', help='output csv file',
  required=True)
parser.add_argument('--raster', help='raster file to use', 
  required=True)
args = parser.parse_args()

logging.info("opening %s" % args.raster)
gtif = gdal.Open(args.raster)
band = gtif.GetRasterBand(DEFAULT_BAND)
nodata = band.GetNoDataValue()
logging.info("nodata value = %s" % nodata)

cols = gtif.RasterXSize
rows = gtif.RasterYSize
logging.info("raster size = %s" % str((cols, rows)))

transform = gtif.GetGeoTransform()
x_origin = transform[0]
y_origin = transform[3]
logging.info("origin point = %s" % str((x_origin, y_origin)))

pixel_w = transform[1]
pixel_h = -transform[5]
logging.info("pixel width = %s" % str((pixel_w, pixel_h)))

data = band.ReadAsArray(0, 0, cols, rows)

logging.info("opening and reading %s" % args.input_csv)
with open(args.input_csv, 'r') as fh:
  csv_r = csv.DictReader(fh)
  fields = csv_r.fieldnames + [args.raster]

  with open(args.output_csv, 'w') as fh_w:
    csv_w = csv.DictWriter(fh_w, fieldnames = fields)
    csv_w.writeheader()

    for line in csv_r:
      assert 'latitude' in line.keys(), "no latitude column"
      assert 'longitude' in line.keys(), "no longitude column"
      x = float(line['longitude'])
      y = float(line['latitude'])

      col = int((x - x_origin) / pixel_w)
      row = int((y_origin - y) / pixel_h)
      value = data[row][col]
      if value == nodata: 
        value = None
      line[args.raster] = value
      csv_w.writerow(line)

  logging.info("file scoring complete!") 

logging.info("writing to file %s" % args.raster)
