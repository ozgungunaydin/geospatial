# SETTING ADDITIONAL NO DATA VALUE OF A RASTER TO ZERO
# ____________________________________________________________________________________________________________
# if layer is active, get the active layer
# layer = iface.activeLayer()
# if layer is not active, get layer by its name
layer = QgsProject.instance().mapLayersByName('DEM_Abruzzo')[0]

# map a list of requested data items from layer
provider = layer.dataProvider()
# the first is band number, the second is a desired number to set to no data
provider.setNoDataValue(1, 0)
# repaint layer
layer.triggerRepaint()
# ____________________________________________________________________________________________________________