# ADDING ALL TIF FILES FROM A FOLDER
# ____________________________________________________________________________________________________________
import os
import glob

# assign the path contaning TIF files to a variable
input_rasters = 'D:/Sapienza/Thesis/OpenData/MODELLO DIGITALE DEL TERRENO - RISOLUZIONE 10X10 METRI/'

# change the current working directory
os.chdir(input_rasters)

print('adding all TIF files...')
# iterate through the files with .tif extension
for fname in glob.glob('*.tif'):
	# get the target path of the specific raster
    uri = input_rasters + fname
    # assign a name to it
    name = fname.replace('.tif', '')
    # add raster layer into the project
    rlayer = iface.addRasterLayer(uri, name)
print('done!')
# ____________________________________________________________________________________________________________