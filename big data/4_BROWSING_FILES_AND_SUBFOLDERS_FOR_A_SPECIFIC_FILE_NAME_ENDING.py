# BROWSING FILES AND SUBFOLDERS FOR A SPECIFIC FILE NAME ENDING
# ____________________________________________________________________________________________________________
# os module contains functions relating to operating system
import os

# create a list of all files with .shp extension containing buildings
all_buildings_shp = []

# set your main file path
main_file = 'some_folder_name'
# for all the files in subfolders of the main folder
for (roots, dirs, files) in os.walk(main_file):
	# iterate one by one
    for file in files:
    	# if file name ends with 'EDIFICI.shp'
    	if file.endswith('EDIFICI.shp'):
    		# add the file name path to the list
    		all_buildings_shp.append(roots + '/' + file)
# ____________________________________________________________________________________________________________