import requests
from xml.dom import minidom
from urllib.parse import urlparse
import os

datadir = './data_rechtsprechung'
tocUrl = 'https://www.rechtsprechung-im-internet.de/rii-toc.xml'
tocFile = os.path.join(datadir, 'rii-toc.xml')

if not os.path.isdir(datadir):
    print ('Creating data dir ...')
    os.mkdir(datadir)
    print('Done')

# Download TOC:
print('updating TOC ...')
r = requests.get(tocUrl)
with open(tocFile, 'wb') as f:
    f.write(r.content)
print('Done: ' + str(r.status_code))

print('reading TOC ...')
doc = minidom.parse(tocFile)
items = doc.getElementsByTagName('link')
numItems = len(items)
print('found '+ str(numItems) +' items')

print('downloading items ...')
for idx,item in enumerate(items, start=1):
    itemurl = item.firstChild.nodeValue
    itemFile = os.path.join(datadir, itemurl[len('http://www.rechtsprechung-im-internet.de/'):])
    itemDir = os.path.dirname(itemFile)
    if not os.path.exists(itemDir):
        os.makedirs(itemDir)
    if not os.path.exists(itemFile):
        print('Downloading item ' + str(idx) + ' of ' + str(numItems))
        r = requests.get(itemurl)
        with open(itemFile, 'wb') as f:
            f.write(r.content)
