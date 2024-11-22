## Initial version.

names = []

for _ in range(3):
    names.append(input("What's your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")


## Next version.

name = input("What's your name?")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

## More Pythonic version.

name = input("What's your name?")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


## Next version.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines: # line is variable and lines is a list.
    print("hello,", line.rstrip())


## Next version.

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


## Sorted version.

name = []

with open ("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


## Sorted with reverse sorted.

name = []

with open ("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for name in sorted(names, reverse=True): # reverse are true.
    print(f"hello, {name}")


## Compact version.

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())


