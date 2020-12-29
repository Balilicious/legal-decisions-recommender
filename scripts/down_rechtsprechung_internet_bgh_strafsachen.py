#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Downloads BGH decisions concerning criminal affairs
from rechtsprechung-im-internet.de
"""

import requests
from xml.dom import minidom
from urllib.parse import urlparse
import os

datadir = 'orig_data/data_rechtsprechung_bgh_strafsachen'
tocUrl = 'https://www.rechtsprechung-im-internet.de/rii-toc.xml'
tocFile = os.path.join(datadir, 'rii-toc.xml')

if not os.path.isdir(datadir):
    print ('Creating data dir ...')
    os.mkdir(datadir)
    print('Done')

# download table of contents:
print('updating TOC ...')
r = requests.get(tocUrl)
with open(tocFile, 'wb') as f:
    f.write(r.content)
print('Done: ' + str(r.status_code))

print('reading TOC ...')
doc = minidom.parse(tocFile)
courts = doc.getElementsByTagName('gericht')
links = doc.getElementsByTagName('link')
numCourts = len(courts)
numLinks = len(links)
print('found '+ str(numLinks) +' links')
print('found '+ str(numCourts) +' courts')
courtsWithLinks = list(zip(courts, links))
numCourtsWithLinks = len(courtsWithLinks)
print('found '+ str(numCourtsWithLinks) +' courts with links')

print('downloading items ...')
for idx,item in enumerate(courtsWithLinks, start=1):
    itemcourt = item[0].firstChild.nodeValue
    # download BGH decisions concerning Strafsachen only:
    if itemcourt.startswith("BGH") and itemcourt.endswith("Strafsenat"):
        itemurl = item[1].firstChild.nodeValue
        itemFile = os.path.join(datadir, itemurl[len('http://www.rechtsprechung-im-internet.de/'):])
        itemDir = os.path.dirname(itemFile)
        if not os.path.exists(itemDir):
            os.makedirs(itemDir)
        if not os.path.exists(itemFile):
            print('Downloading item ' + str(idx) + ' of ' + str(numLinks) + ' from ' + itemcourt)
            r = requests.get(itemurl)
            print(r.status_code)
            with open(itemFile, 'wb') as f:
                f.write(r.content)
