## Initial version

i = 3 
while i != 0:
    print("meow")
    i = i - 1

## Second version

i = 1
while i < 3:
    print("meow")
    i += 1 

## Third version "for" loop

for i in range(3):  # range function, # using underscore _ when you dont need to name variable, and its signal that you dont care ybout its name.
    print("meow")

## Fourth version

print("meow\n" * 3, end="") 

## Fifth version

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range (n):
    print("meow")

## Sixsth version

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        return n


def meow(n):
    for _ in range(n):
        print("meow")


main()




        




