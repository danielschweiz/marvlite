import numpy as np
frim astropy.io import fits
from astropy.wcs import WCS

import marvin

from .core import MarvinToolsClass
from .mixins import GetApertureMixIn, NSAMixIn


class Cube(MarvinToolsClass):
  
  def __init__(self, input=None, filename=None, 
               #mangaid=None, plateifu=None, mode=None, #release=None, drpall=None, download=None, nsa_source='auto',
               #wont be based on manga, user will have the file downloaded. drpall is used for finding spectra from manga database? 
               data=None)

    self.header = None
    self.wcs = None
    self._wavelength = None
    self._shape = None

    self._extension_data={}

    self._flux = None
    self._spectral_resolution = None
    self._spectral_resolution_prepixel = None
    self._dispersion = None
    self._dispersion_prepixel = None

    self._bitmasks = None

    MarvinToolsClass.__init__(self, input=input, filename=filename, 
                              #mangaid=mangaid, plateifu=plateifu, mode=mode, release=release, drpall=drpall, download=download,
                             data=data)





