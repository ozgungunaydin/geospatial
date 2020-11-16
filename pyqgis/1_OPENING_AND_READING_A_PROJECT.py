# OPENING AND READING A PROJECT
# ____________________________________________________________________________________________________________
import os

# assign the project instance and prints the current file name
project = QgsProject.instance()
print(project.fileName())

# return the current working directory
print(os.getcwd())

# read the project in a given path
print('reading the project...')
project.read('D:/Sapienza/Thesis/Ozgun_Study/Lanciano.qgz')
print(project.fileName())
print('done!')
# ____________________________________________________________________________________________________________