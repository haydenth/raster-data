raster-data
=================
Pretty simple python script to extract data from a raster file based on csv with lat/lng

Requirements
=================
This tool requires osgeo GDAL and OGR python packages. [Download and Installation Instructions](https://www.gdal.org/)

Running
===============
When running this script, it takes 3 parameters:

* raster: path to the raster file you want to run the csv over
* input-csv: path to the input csv
* output-csv: path to the output csv where the data is to be appended

```
$ python get-value.py --raster PHIHOX_M_sl7_250m_Saudi.tif --input-csv sample.csv --output-csv result.csv
```

When you run, it should output data to confirm it's running.
```
INFO:root:opening PHIHOX_M_sl7_250m_Saudi.tif
INFO:root:nodata value = 255.0
INFO:root:raster size = (10126, 7572)
INFO:root:origin point = (34.569064635703086, 32.15437606213837)
INFO:root:pixel width = (0.0020833566163945072, 0.0020832077447607844)
INFO:root:opening and reading sample.csv
INFO:root:file scoring complete!
INFO:root:writing to file PHIHOX_M_sl7_250m_Saudi.tif
```

Contact
==============
Questions, contact thayden@gmail.com
