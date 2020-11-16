# ADDING OPEN STREET MAP LAYER INTO THE PROJECT
# ____________________________________________________________________________________________________________
# osm url with its parameters
urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
# create an osm layer variable
osmlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  

# add osm to the project if the corresponding variable is correct
if osmlayer.isValid():
	print('adding open street map...')
    QgsProject.instance().addMapLayer(osmlayer)
    print('done!')
else:
    print('invalid layer')
# ____________________________________________________________________________________________________________