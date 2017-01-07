import json
import sys
import re

jsonver = 3

if sys.argv[1].endswith(".json"):
    with open(sys.argv[1]) as data_file:
        data = json.load(data_file)['version']
        filever = re.search(r"\d+(\.\d+)?", data).group(0)
        print "File version is (", filever, ") compared to live version (", jsonver, ")."

else:
    print "Error, not a json file"



#if jsonfile.endswith(sys.argv[1]):
#    print "This is a json file"
#else:
#    print "This is not a json file"
