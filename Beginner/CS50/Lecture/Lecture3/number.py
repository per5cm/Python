## Exception

try:
    x = int(input("What's x?: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")

## Next Version using 'else' conditional

try:
    x = int(input("What's x?: "))  
except ValueError:
    print("x is not an interger")

else:
    print(f"x is {x}")

## Refine it little bit futher using a loop

while True:
    try:
        x = int(input("What's x?: "))  
    except ValueError:
        print("x is not an interger")
    else:
        break
        
print(f"x is {x}")

## Refine it futhuremore

def main():
    x = get_int()
    print(f"x is{x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?: "))  
        except ValueError:
            print("x is not an interger")
        else:
            return x   # return is stronger than break
        
main()

## Even futhermore refinenment

def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            return int(input("What's x?: "))            
        except ValueError:
            print("x is not an interger")
        
main()

## Other Version using 'pass'

def main():
    x = get_int()
    print(f"x is{x}")

def get_int():
    while True:
        try:
            return int(input("What's x?: "))            
        except ValueError:
            pass
        
main()

## final refinment

def main():
    x = get_int("What's x?: ")
    print(f"x is{x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))            
        except ValueError:
            pass
        
main()

