__author__ = 'yalamanchili'
__author__ = 'prasanth'

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:14:53 2015

@author: Sam
"""
#import string
import re

patterns = re.compile('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]')

#text = "AAAaAAA"

with open("test.txt") as text:
    m = patterns.finditer(text.read())

for i in m:
    print(i.group())
