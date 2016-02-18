#!/usr/bin/env python

# It is assumed that this repo is cloned into a child directory of the main 
# website directory. This program copies all html files from the cloned repo
# to the website.

from shutil import copy2
from glob import glob

for file in glob(r'*.html')
    print file
