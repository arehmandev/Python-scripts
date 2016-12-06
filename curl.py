from StringIO import StringIO
import pycurl
import json
import re
import sys

url = 'https://s3-eu-west-1.amazonaws.com/kaplandevopstest/version.json'

storage = StringIO()
version = pycurl.Curl()
version.setopt(version.URL, url)
version.setopt(version.WRITEFUNCTION, storage.write)
version.perform()
version.close()
content = storage.getvalue()

jsonmixed = json.loads(content)['version']
s = re.search(r"\d+(\.\d+)?", jsonmixed)
versionjson = s.group(0)


if len(sys.argv) !=2:
    print "This script is used to compare version.json to live"
    print "Type in 'python curl.py help' for options"

elif sys.argv[1] == "help":
    print "Your options are as follows:"
    print "1 - 'python curl.py version' - This shows the current live version.json number"
    print "2 - 'python currency.py 1.11' - Replace 1.11 with the version you wish compare to live"
    print "Note: All currencies are compared live with EUROS as the base value of 1"

elif sys.argv[1] == "version":
    print versionjson
    print "For more options, type 'python curl.py help'"

elif sys.argv[1] < versionjson:
    print "Live version is newer"
    print sys.argv[1], "<", versionjson

elif sys.argv[1] > versionjson:
    print "Live version is older"
    print sys.argv[1], ">", versionjson

else:
    print "How on earth did you get here"
    print "Type in 'python curl.py help' for options"
