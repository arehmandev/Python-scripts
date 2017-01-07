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
    print "2 - python curl.py version.json - Reads json file version"

elif sys.argv[1] == "version":
    print versionjson
    print "For more options, type 'python curl.py help'"

elif sys.argv[1].endswith(".json"):
    with open(sys.argv[1]) as data_file:
        data = json.load(data_file)['version']
        filever = re.search(r"\d+(\.\d+)?", data).group(0)
        print "File version is (", filever, ") compared to live version (", versionjson, ")."

else:
    print "Error, how on earth did you get here"
    print "Type in 'python curl.py help' for options"
