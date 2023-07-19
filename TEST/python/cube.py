import os

class DataCube:
    '''Class that can pull all necessary functional information from an inputted datacube.'''

    def __init__ (self, file_name):   
        file_name = None

    def get_filename(self, fullpath):
         '''Gets filename from a given file path. Planning on adding a check to confirm whether or not the file is a .fits.gz file.'''      
         filename = os.path.basename(fullpath)
         return filename
    