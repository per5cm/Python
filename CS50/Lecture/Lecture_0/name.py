## Ask user for their name

name = input("What's your name? ")

## Say hello to user
print ("hello, " + name) ## first aproach with + operator
print ("hello,", name) ## second aproach
print ("hello, ", end="") ## third aproach
print (name)
print("hello,", name, sep="???") ## override the default behavior of SEP.

## Final Version!

name = input("What's your name? ")

## Problem: to clean space if users presses too much space button.
## Remove whitespace from string

name = name.strip() ## variable with function called method

## Capitalize user's name (you could use .capitalize() but it only capitalize first word)

name = name.strip().title()

print(f"hello, {name}") ## f is for F-string.

## Shorter Version

name = input("What's your name? ").strip().title()
print(f"hello, {name}")

## Version where computer print only first name

name = input("What's your name? ").strip().title()

## Split user's name into first name and last name

first, last = name.split(" ")

print(f"hello, {first}")


