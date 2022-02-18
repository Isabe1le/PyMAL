"""
MyAnimeList API Wrapper
~~~~~~~~~~~~~~~~~~~~~~~

An asynchronous Python API wrapper for MyAnimeList.

:copyright: (c) 2022-present Scrumpyy
:license: MIT, see LICENSE for more details.

"""

__title__ = 'pymal'
__author__ = 'Scrumpyy'
__license__ = 'MIT'
__copyright_ = 'Copyright 2022-present Scrumpyy'
__version__ = '0.0.1'

import logging

from .mal import *

logging.getLogger(__name__).addHandler(logging.NullHandler())