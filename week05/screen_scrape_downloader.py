"""
Assignment: choose one or both or all three. I suspect 2 is a lot harder, but 
then you would have learned a lot about the GitHub API and JSON.

1. File downloader using screen scraping: write a script that scrapes
our Python Winter 2012 course page for the URLs of all the Python
source files, then downloads them all.

"""

import urllib2
import re
from pprint import pprint
from BeautifulSoup import BeautifulSoup
import os
import time

if os.path.exists("downloads"):
    os.system("rm -rf downloads")
os.system("mkdir downloads")

# read a web page into a big string
page = urllib2.urlopen('http://jon-jacky.github.com/uw_python/winter_2012/index.html').read()

# parse the string into a "soup" data structure
soup = BeautifulSoup(page)

# find all the anchor tags in the soup
anchors = soup.findAll('a')

# find all the anchor tags that link to external web pages
externals = soup.findAll('a',attrs={'href':re.compile('http.*')})

# find all the anchor tags that link to Python files
pythonfiles = soup.findAll('a',attrs={'href':(lambda a: a and a.endswith('.py'))})

for files in pythonfiles:
    s = str(files)
    file_path = s[s.find('=') + 2 : s.find('>') -1]
    time.sleep(1)
    url = 'http://jon-jacky.github.com/uw_python/winter_2012/' + file_path
    print url

    fileContent = urllib2.urlopen(url)
    
    dir = os.path.dirname(file_path)
    if not os.path.exists("downloads/" + dir):
        os.system("mkdir -p downloads/%s" %dir)
    f = open("downloads/"+ dir + "/" + os.path.basename(file_path), "wb")
    meta = fileContent.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_path, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = fileContent.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    f.close()


