import numpy as np
frim astropy.io import fits
from astropy.wcs import WCS

import marvin

from .core import MarvinToolsClass
from .mixins import GetApertureMixIn, NSAMixIn


class Cube(MarvinToolsClass):
  
  def __init__(self, input=None, filename=None, mangaid=None, plateifu=None,
               mode=None, data=None, release=None, 
               drpall=None, download=None, nsa_source='auto')

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

