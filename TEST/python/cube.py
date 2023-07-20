import os
from astropy.io import fits

class DataCube:
    '''Class that can pull all necessary functional information from an inputted datacube.'''

    def __init__ (self, file_name):   
        file_name = None

    def get_filename(self, fullpath):
         '''Gets filename from a given file path. Checks to confirm whether or not the file is a .fits.gz file.'''      
         filename = os.path.basename(fullpath)
         if filename.endswith('.fits.gz'):
             return filename
         else:
             return 'This file is not a datacube (.fits.gz) file.'
         
    def open_gz(self, filename):
        '''Opens .fits.gz files'''
