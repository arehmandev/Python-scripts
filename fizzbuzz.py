import sys
count = sys.argv[1]

if int(count) % 5 == 0 and int(count) % 3 == 0:
    print "FizzBuzz"
elif int(count) % 3 == 0:
    print "Fizz"
elif int(count) % 5 == 0:
    print "Buzz"
else:
    print "Not a multiple of 5 or 3"
