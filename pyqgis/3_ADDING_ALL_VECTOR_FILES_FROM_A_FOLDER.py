# ADDING ALL VECTOR FILES FROM A FOLDER
# ____________________________________________________________________________________________________________
import os
import glob

# assign the path contaning raster files to a variable
input_vectors = 'D:/Sapienza/Thesis/Ravagnan/1st Files/TAV1OZGUN/'

# change the current working directory
os.chdir(input_vectors)

print('adding all vector files...')
# iterate through the files with .shp extension
for fname in glob.glob('*.shp'):
	# get the target path of the specific vector
    uri = input_vectors + fname
    # assign a name to it
    name = fname.replace('.shp', '')
#    vlayer = QgsVectorLayer(uri, name, 'ogr')
#    QgsProject.instance().addMapLayer(vlayer)
# 2nd alternative to the last two lines:
    vlayer = iface.addVectorLayer(uri, name, 'ogr')
print('done!')
# ____________________________________________________________________________________________________________