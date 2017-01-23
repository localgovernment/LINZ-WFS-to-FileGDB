import os
import sys
import time

def linz_wfs_to_fgdb(datadir, aspatial, spatial, APIKey, bbox):
       
    dirfmt = "%4d-%02d-%02d-%02d%02d%02d"
    fullpath = os.path.join(datadir, dirfmt % time.localtime()[0:6])
    os.mkdir(fullpath)

    ogrhead = r'ogr2ogr -overwrite -skipfailures -f "FileGDB" "%s.gdb" "http://wfs.data.linz.govt.nz/{}/v/x%s/wfs?service=WFS&version=1.0.0&request=GetFeature&typeName=v:x%s'.format(APIKey)
    
    ogrwfsspat = r'&SRSNAME=EPSG:2193&bbox={}'.format(bbox)
    
    ogrtail = r'" -nln "x%s" -a_srs EPSG:2193'

    aspatial_tables = []
    spatial_tables = []

    for linz_service in linz_aspatial + linz_spatial:
        ogrstring = ogrhead
        linz_table = r"x%s.gdb\x%s" % (linz_service, linz_service)
        if linz_service in linz_spatial:
            ogrstring = ogrstring + ogrwfsspat
            spatial_tables.append(linz_table)
        else:
            aspatial_tables.append(linz_table)
            
        ogrstring = ogrstring + ogrtail
        cmd = ogrstring % (os.path.join(fullpath, 'x' + linz_service), linz_service, linz_service, linz_service)
        os.system(cmd)

    return fullpath, aspatial_tables, spatial_tables


if __name__ == "__main__":

    # data output directory (example):
    datadir = r"D:\Temp\Data"    
    
    # LINZ aspatial dataset numbers (example below 3371 = road names table):
    linz_aspatial = ['3371']
    
    # LINZ spatial dataset numbers (example below 794 = survey plans and 1571 = NZ parcels ):
    linz_spatial = ['794','1571']

    # LINZ API key:
    APIKey = 'your LINZ API key here'
    
    # bounding box (following is Taupo area):
    bbox = '175.4563,-39.3846,176.7543,-38.2131'

    fullpath, aspatial_tables, spatial_tables = linz_wfs_to_fgdb(datadir, linz_aspatial, linz_spatial, APIKey, bbox)

    print(fullpath)
    print(aspatial_tables)
    print(spatial_tables)
