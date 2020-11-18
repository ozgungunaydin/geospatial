# ADDING VECTOR FILES TO PROJECT FROM A LIST
# ____________________________________________________________________________________________________________
# iterate through list of paths to be used
for building_shp in all_buildings_shp:
    # assign name variable to current item
    name = building_shp.replace('.shp', '')
    # add current vector to the project (path, name, ogr library (for shapefile and many other file formats))
    vlayer = iface.addVectorLayer(building_shp, name, 'ogr')
# ____________________________________________________________________________________________________________