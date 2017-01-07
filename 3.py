import json
import sys

miles_dict = {'Monday':1, 'Tuesday':2.3, 'Wednesday':3.5, 'Thursday':0.9}
#for k, v in miles_dict.items():
#    print("%s: %s" % (k, v))
coded = json.dumps(miles_dict)
decoded = json.loads(coded)[sys.argv[1]]

print decoded
