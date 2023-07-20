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
         
    def open_gz(self):
        '''Opens .fits.gz files and spits back the full header.'''
        path = input('file path:')
        with fits.open(path) as f:
            f.info()

    def pixflux(self, path, x, y):
        '''Inputs x and y coordinates and gets exact flux for that pixel.'''
        path = input('file path:')
        hdul = fits.open(path)
        data = hdul[1].data
        posdata = data[y - 1, x - 1]
        print(f"the flux at x = {x} and y = {y} is {posdata:.0f}")