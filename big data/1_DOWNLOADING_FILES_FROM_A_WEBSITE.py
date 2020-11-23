# DOWNLOADING FILES FROM A WEBSITE
# ____________________________________________________________________________________________________________
# OS module provides functions for interacting with the operating system.
import os
# Requests is an HTTP library
import requests
# urllib.request is a Python module for fetching URLs
# import urllib.request
# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# set a specific url
url = 'http://opendata.regione.abruzzo.it/opendata/Modello_digitale_del_terreno_risoluzione_10x10_metri/'

# request data from server
r = requests.get(url)
# html.parser module defines a class HTMLParser which serves as the basis
# for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML
soup = BeautifulSoup(r.text, 'html.parser')

# The HREF contains two components: the URL, which is the actual link,
# and the clickable text that appears on the page, called the "anchor text."
all_hrefs = soup.find_all('a')
# get the urls of all identified href tags
all_links = [link.get('href') for link in all_hrefs]
# The dl module is for handling dynamically linked libraries.
rar_files = [dl for dl in all_links if dl and '.rar' in dl]
# target folder
download_folder = 'D:/some_folder_name'

# check if specified path exists
if not os.path.exists(download_folder):
    # create a directory if it doesn't
    os.makedirs(download_folder)

print('downloading the files...')
# iterate through rar files
for rar_file in rar_files:
    # request data from server
    r = requests.get(rar_file)
    # os.path.basename method is used to get the base name in specified path. This method
    # internally use os.path.split() method to split the specified path into a pair (head, tail)
    # and it returns the tail part after splitting the specified path into (head, tail) pair.
    rar_filename = os.path.basename(rar_file)
    # sets a path by joining target folder and file name
    dl_path = os.path.join(download_folder, rar_filename)
    # open the file to write in binary mode as an uncompressed file
    with open(dl_path, 'wb') as z_file:
        print('link: ', rar_file, '\nfile name: ', rar_filename)
        # write the content of the requested file to the specified file
        z_file.write(r.content)
print('done!')

# if we were going to download a single file from a single url:

# url = 'http://opendata.regione.abruzzo.it/opengeodata/Dati_raster/2007%20-%20DTM%2010x10/326150_DTM10x10.rar'
# print('downloading the file with urllib2...')
# urllib.request.urlretrieve(url,'D:/some_folder_name')
# print('done!')
# ____________________________________________________________________________________________________________
