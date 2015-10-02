# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:00:32 2015

@author: prasanth-varikallu
"""

with open("test.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      #print("End of file")
      break
    else:
        if (ord(c) in range(97,123) or ord(c) in range(65,91)):
            print(c,end="")
print()
