import urllib2
import json
import sys

curl = urllib2.urlopen('http://api.fixer.io/latest')
moneyjson = json.load(curl)['rates']

if len(sys.argv) !=2:
    print "This script is used to compare live currency exchange rates"
    print "Type in 'python currency.py help' for options"

elif sys.argv[1] == "help":
    print "Your options are as follows:"
    print "1 - 'python currency.py list' - This lists all currencies and their values"
    print "2 - 'python currency.py ABC' - Replace ABC with the 3 letter currency code to get value e.g. GBP"
    print "Note: All currencies are compared live with EUROS as the base value of 1"

elif sys.argv[1] == "list":
    for k, v in sorted(moneyjson.items()):
        print("%s: %s" % (k, v))

elif len(sys.argv) == 2:
    argument = sys.argv[1]
    capitalized = argument.upper()
    try:
        print capitalized, ":", moneyjson[capitalized]
    except Exception, e:
        print "That is an invalid currency code. Try a real one e.g. GBP"
        print "Type in 'python currency.py help' for options"

else:
    print "How on earth did you get here"
    print "Type in 'python currency.py help' for options"
