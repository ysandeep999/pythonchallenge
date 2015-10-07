__author__ = 'yalamanchili'
__author__ = 'prasanth'

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:14:53 2015

@author: San
"""
#import string
import re

patterns = re.compile('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]')

#text = "AAAaAAA"

with open("4test.txt") as text:
    m = patterns.finditer(text.read())

bsb =[]

for i in m:
    bsb.append(i.group())
    #print(i.group())
print(bsb)
print(len(bsb))


for word in bsb:
    if(word[0] == word[6] and word[1] == word[5]): # and word[2] == word[6]):
        print(word)

patlist = []

def patlinefinder(line):        # 
    patt = re.compile('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]')
    res = re.search(patt, line)
    res.groups()
    if (res):
        patlist.append(res)

emptlst =[]
def patlinefind(line):
    patt = re.compile('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]')
    linelen = len(line)
    for l1 in range(0,linelen - 7):
        if(line[l1].isupper() and line[l1 + 1].isupper() and line[l1 + 2].isupper() and line[l1 + 3].islower() and line[l1 + 4].isupper() and line[l1 + 5].isupper() and line[l1 + 6].isupper()):
            #emptlst.append(line[l1:l1 + 7])
            emptlst.append((line[l1:l1 + 7],line[l1:l1+3],line[l1+4:l1+7]))
            #print(line[l1:l1 + 7])
            #print(len(emptlst))
            ##if(line[l1] == line[l1 + 4] and line[l1 + 1] == line[l1 + 5] and line[l1 + 2] == line[l1 + 6]):
              #  print(line)


def pal(lst):
    for full in lst:
        if(full[1][0] in full[2] and full[1][2] in full[2]  and full[1][1] in full[2]):
            print(full)


def beginhere():
    f = open('4test.txt', 'r')
    #num = {}
    for line in f:
        #patlinefinder(line)
        patlinefind(line)

    #print(patlist[1])
    print(emptlst)
    print(len(emptlst))
    pal(emptlst)

beginhere()