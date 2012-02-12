"""
gitHub_downloader_by_api.py
File downloader using web API: same as 1, but find the Python source
files using the GitHub API.  Hints: you need to look in the repo at
https://github.com/jon-jacky/uw_python/tree/gh-pages, not the web
pages.  Git calls the files in a repository "blobs", see the "get all blobs"
example about halfway down this page: http://develop.github.com/p/object.html

"""
import urllib2
import os
import time
from pprint import pprint

# this user has several repos. URL here is a GitHub API call
url = 'http://github.com/api/v2/json/blob/all/jon-jacky/uw_python/gh-pages'
handle = urllib2.urlopen(url)
data = handle.read()
d = eval(data)

if os.path.exists("downloads"):
    os.system("rm -rf downloads")
os.system("mkdir downloads")

pythonFileList = []
dict = d["blobs"]
for fileName in dict.keys():
    extension = os.path.splitext(fileName)[1][1:]
    if extension == "py":
	pythonFileList.append(fileName)

for file_path in pythonFileList:
    sha = dict[file_path]
    time.sleep(1)
    url = 'http://github.com/api/v2/json/blob/show/jon-jacky/uw_python/' + sha
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

