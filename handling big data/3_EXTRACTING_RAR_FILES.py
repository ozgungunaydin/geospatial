# EXTRACTING RAR FILES
# ____________________________________________________________________________________________________________
# run the following on your windows command prompt (cmd) if you don't have patool: pip install patool

import os
import patoolib

# set a working directory
dir_name = 'D:/some_folder_name'
# filetype to be extacted
extension = ".rar"

# change the current working directory
os.chdir(dir_name)

# listdir method gets the list of all files from mentioned directory
# iterate through the list of files in the given directory
print('extracting the files...')
for item in os.listdir(dir_name):
    # if the current item has the aforementioned extension
    if item.endswith(extension):
        # return the full path of the file
        file_name = os.path.abspath(item)
        # extract file to target folder
        patoolib.extract_archive(file_name, outdir=dir_name)
        # delete rar file
        os.remove(file_name)
print('done!')
# ____________________________________________________________________________________________________________