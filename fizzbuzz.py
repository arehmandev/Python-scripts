import sys
count = sys.argv[1]

divider1 = 3
divider2 = 5

if int(count) % int(divider1) == 0 and int(count) % int(divider2) == 0:
    print "FizzBuzz"
elif int(count) % int(divider1) == 0:
    print "Fizz"
elif int(count) % int(divider2) == 0:
    print "Buzz"
else:
    print "Not a multiple of", int(divider1), "or", int(divider2)
