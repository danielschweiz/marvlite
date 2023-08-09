 # spaxel stuff
from cube import DataCube as dc
from astropy.io import fits
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

    def specvis(self, x, y):
        path = input('file path:')
        hdul = fits.open(path)
        flux = hdul[1].data
        spectrum = flux[:, x, y]
        units=hdul[1].header['BUNIT']
        plt.plot(spectrum)
        plt.xlabel('Wavelength (Å)')
        plt.ylabel(f'Flux ({units})')
        plt.show()
         
    

