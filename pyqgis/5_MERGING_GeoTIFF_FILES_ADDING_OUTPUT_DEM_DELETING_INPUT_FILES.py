# MERGING GeoTIFF FILES USING A PROCESSING TOOL, ADDING OUTPUT DEM FILE INTO THE PROJECT
# AND DELETING INPUT FILES USED FOR PROCESSING
# ____________________________________________________________________________________________________________
# set folder path with consisting number of dem files to merge
input_dem_files = 'D:/Sapienza/Thesis/OpenData/MODELLO DIGITALE DEL TERRENO - RISOLUZIONE 10X10 METRI/'
# set the extension of input files
extension = '.tif'
# set the output file path
output_dem_file = 'D:/Sapienza/Thesis/Ozgun_Study/DEM_Abruzzo.tif'

# return pointer to the root (invisible) node of the project's layer tree
root = QgsProject.instance().layerTreeRoot()
# create a list to add all dem files
all_dem_files = []
# iterate over the tag’s children using the .children generator
for layer in root.children():
	# if the layer's name starts with 'WGS84_DTM10x10_'
	if layer.name().startswith('WGS84_DTM10x10_'):
		# add full layer path to the list
		all_dem_files.append(input_dem_files + layer.name() + extension)

print('merging dem files...')
# set parameters for processing
params = { 'DATA_TYPE' : 5, 'EXTRA' : '', 'INPUT' : all_dem_files, 'NODATA_INPUT' : None, 'NODATA_OUTPUT' : None,
'OPTIONS' : '', 'OUTPUT' : output_dem_file, 'PCT' : False, 'SEPARATE' : False }
# run processing with gdal, merge utility
processing.run('gdal:merge', params)
print('done!')

print('adding output dem file...')
# add output file to the project
rlayer = iface.addRasterLayer(output_dem_file, output_dem_file[-15:-4])
print('done!')

print('removing all unnecessary dem files except the output...')
# create a dictionary with all layers in the project
layers = QgsProject.instance().mapLayers()
# iterate through all layers
for layer in layers:
	# if the layer name starts with ...
	if layer.startswith('WGS84_DTM10x10_'):
		# delete it from the project
		QgsProject.instance().removeMapLayer(layer)
print('done!')
# ____________________________________________________________________________________________________________