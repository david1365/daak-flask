# -*- coding: utf-8 -*-
"""
    daak
    ~~~~~

    A microframework based on twisted.  It's extensively documented
    and follows best practice patterns.

    :copyright: (c) 2017 by Davood Akbari.
    :license: GPL, see LICENSE for more details.
"""
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "27 November 2017"

config = {}
execfile("../../config/config.py", config)

try:
    rootDirectory = config['rootDirectory']
except:
    # TODO: complet this line and show miss variable
    raise ValueError("please set need variables in config file!")

from glob import glob
from os.path import basename, dirname, join
from os import walk

# print glob(join(rootDirectory, "/*/"))
#
# dir_list = next(walk(rootDirectory))
# print dir_list, walk(rootDirectory)

# my_list = [x for x in my_list if x.attribute == value]
importFiles = [file for root, dirs, files in walk(rootDirectory) if file != "config.py"]
    # print root
    # print dirs
print importFiles
