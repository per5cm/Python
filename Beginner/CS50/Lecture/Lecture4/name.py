## command-line arguments sys.argv

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


## Alternate Version with refined error messages.

import sys

#check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello,my name is", sys.argv[1])

## alternate version using sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

## alternate version using slice

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:    # here you slice the list to position 1. list wont start from position 0. if you use negative you slice from other direction of the list. 
    print("hello, my name is", arg)