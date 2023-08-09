 # spaxel stuff
from cube import DataCube as dc
import numpy as np
import matplotlib.pyplot as plt

class Spaxel(filename):

    def __init__(self, x, y, cube=True, maps=True):
        self._cube = cube
        self._maps = maps
        self.x=int(x)
        self.y=int(y)

    def flux(self, x, y):
        '''Gets flux cube, and, if specified, gets spectrum.'''
        if x == y == None or x == y == []:
            path = input('file path:')
            hdul = fits.open(path)
            data = hdul[1].data
            print(data)
        else:
            path = input('file path:')
            hdul = fits.open(path)
            data = hdul[1].data
            x = int(x)
            y = int(y)
            spectrum = data[:, x, y]
            print(spectrum)

     def specvis(self, x, y)
         '''Plots'''
            hdul = fits.open('manga-8485-1901-LOGCUBE.fits.gz')
            flux = hdul[1].data
            spectrum = flux[:, x, y]
            plt.plot(spectrum)
    
    self.spectrum= self.cube(self.x,self.y)
