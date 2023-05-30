import astropy.io.fits

import marvin

__ALL__ = ['MarvinToolsClass']


def kwargsGet(kwargs, key, replacement):
    """As kwargs.get but uses replacement if the value is None."""

    if key not in kwargs:
        return replacement
    elif key in kwargs and kwargs[key] is None:
        return replacement
    else:
        return kwargs[key]

class MarvinToolsClass(MMAMixIn, CacheMixIn):
    """Marvin tools main base class.

    This super class implements the :ref:`decision tree <marvin-dma>`
    for using local files, database, or remote connection when
    initialising a Marvin tools object.

    Parameters:
        input (str):
            A string that can be a filename, plate-ifu, or mangaid. It will be
            automatically identified based on its unique format. This argument
            is always the first one, so it can be defined without the keyword
            for convenience.
        filename (str):
            The path of the file containing the file to load. If set,
            ``input`` is ignored.
        mangaid (str):
            The mangaid of the file to load. If set, ``input`` is ignored.
        plateifu (str):
            The plate-ifu of the data cube to load. If set, ``input`` is
            ignored.
        mode ({'local', 'remote', 'auto'}):
            The load mode to use. See :ref:`mode-decision-tree`.
        data (:class:`~astropy.io.fits.HDUList`, SQLAlchemy object, or None):
            An astropy ``HDUList`` or a SQLAlchemy object, to be used for
            initialisation. If ``None``, the :ref:`normal <marvin-dma>`` mode
            will be used.
        release (str):
            The MPL/DR version of the data to use.
        drpall (str):
            The path to the
            `drpall <https://trac.sdss.org/wiki/MANGA/TRM/TRM_MPL-5/metadata#DRP:DRPall>`_
            file to use. If not set it will use the default path for the file
            based on the ``release``.
        download (bool):
            If ``True``, the data will be downloaded on instantiation. See
            :ref:`marvin-download-objects`.

    Attributes:
        data (:class:`~astropy.io.fits.HDUList`, SQLAlchemy object, or dict):
            Depending on the access mode, ``data`` is populated with the
            |HDUList| from the FITS file, a
            `SQLAlchemy <http://www.sqlalchemy.org>`_ object, or a dictionary
            of values returned by an API call.
        datamodel:
            A datamodel object, whose type depends on the subclass that
            initialises the datamodel.
        data_origin ({'file', 'db', 'api'}):
            Indicates the origin of the data, either from a file, the DB, or
            an API call.
        filename (str):
            The path of the file used, if any.
        mangaid (str):
            The mangaid of the target.
        plateifu:
            The plateifu of the target

    """

breadcrumb = MarvinBreadCrumb()

def __init__(self, input=None, filename=None, mangaid=None, plateifu=None,
                 mode=None, data=None, release=None, drpall=None, download=None):

        MMAMixIn.__init__(self, input=input, filename=filename, mangaid=mangaid,
                          plateifu=plateifu, mode=mode, data=data, release=release,
                          download=download)

        CacheMixIn.__init__(self)

        # drop breadcrumb
        breadcrumb.drop(message='Initializing MarvinTool {0}'.format(self.__class__),
                        category=self.__class__)

        # Load VACs
        from marvin.contrib.vacs.base import VACMixIn
        self.vacs = VACMixIn.get_vacs(self)