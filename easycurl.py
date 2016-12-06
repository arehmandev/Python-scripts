import urllib2
import json
import re

curl = urllib2.urlopen('https://s3-eu-west-1.amazonaws.com/kaplandevopstest/version.json')
versionjson = json.load(curl)['version']


s = re.search(r"\d+(\.\d+)?", versionjson)

print "Version of live is", s.group(0)
