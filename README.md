# LINZ-WFS-to-FileGDB
Download spatial and non-spatial data from LINZ to a file geodatabase

## Install
1. Sign up to https://data.linz.govt.nz/ and get an API key
2. Download Python - tested with ESRI's 2.7.8 version
3. Download 'Generic installer for the GDAL core components' and 'Installer for the GDAL FileGDB plugin' from http://www.gisinternals.com/release.php. At time of writing downloaded:
 * http://download.gisinternals.com/sdk/downloads/release-1800-x64-gdal-2-1-2-mapserver-7-0-2/gdal-201-1800-x64-core.msi
 * http://download.gisinternals.com/sdk/downloads/release-1800-x64-gdal-2-1-2-mapserver-7-0-2/gdal-201-1800-x64-filegdb.msi
4. Install GDAL Core and then Plugin, typical install for both.
5. Modify system path to include "C:\Program Files\GDAL"
6. Add following system environmental variables:
 * GDAL_DATA=C:\Program Files\GDAL\gdal-data
 * GDAL_DRIVER_PATH=C:\Program Files\GDAL\gdalplugins
7. Download [getlinzdata.py](https://raw.githubusercontent.com/localgovernment/LINZ-WFS-to-FileGDB/master/getlinzdata.py) and modify the function parameters within that file
