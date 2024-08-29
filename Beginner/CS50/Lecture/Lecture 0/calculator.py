## Initial version
x = 1
y = 2

z = x + y

print (z)

## Second Version
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)


## Third Version
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

## Forth Version
print(int(input("What's x? ")) + int(input("what's y?")))


## Float Version
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)


## Round Version
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(x + y)

## Format Number

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}") # syntax for format the output of a number

## Rounding first Version

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2) 

print(x + y)

## 'f string' (new thing on python 3)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y 

print(f"{z:.2f}") # Syntax to specify f string how many digits you wanna print

## Return

def main():
    x = int(input("What's x? ")) ## x converts into interger
    print("x squared is", square(x)) ## says x squared and second argument to print function
    
def square(n):
    return n * n ## return value


main()