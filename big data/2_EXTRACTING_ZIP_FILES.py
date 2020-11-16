# EXTRACTING COMPRESSED FILES
# ____________________________________________________________________________________________________________
import os
import zipfile

# set a working directory
dir_name = 'D:/some_folder_name'
# filetype to be extacted
extension = ".zip"

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
        # create zipfile object
        zip_ref = zipfile.ZipFile(file_name)
        # extract file to target folder
        zip_ref.extractall(dir_name)
        # close file
        zip_ref.close()
        # delete zipped file
        os.remove(file_name)
print('done!')

# if we were going to extract one specific zip file:

# path_to_zip_file = insert the path of your zip file
# directory_to_extract_to = insert the path of your target directory

# print('extracting the file...')
# with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
#     zip_ref.extractall(directory_to_extract_to)
# print('done!')
# ____________________________________________________________________________________________________________
