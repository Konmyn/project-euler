#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import glob

os.chdir('/home/ethan/Downloads')
for i in glob.glob('*.rar'):
    print i
