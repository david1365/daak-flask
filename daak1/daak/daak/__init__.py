# -*- coding: utf-8 -*-

__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "27 November 2017"

from daak1.daak.daak.configManager import getContextManager

contextManager = getContextManager()

# config = {}
# execfile("../../config/config1.py", config)
#
# try:
#     rootDirectory = config['rootDirectory']
# except:
#     # TODO: complet this line and show miss variable
#     raise ValueError("please set need variables in config file!")
#
from glob import glob
from os.path import basename, dirname, join
from os import walk

print glob(join(contextManager.rootPath, "/*/"))
#
root, dirs, files = next(walk(contextManager.rootPath))
print root,dirs#, walk(contextManager.rootPath)

for name in dirs:
    print name



def f():
    yield 1, 2, 3

a, b, c = next(f())

print c

# my_list = [x for x in my_list if x.attribute == value]
# importFiles = [file for root, dirs, files in walk(rootDirectory) if file != "config1.py"]
#     # print root
#     # print dirs
# print importFiles
