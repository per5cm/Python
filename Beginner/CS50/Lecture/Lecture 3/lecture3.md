# Exceptions (something awry)

Exceptions used for the things you are not ready for.

Syntax Error // Run time error, what could go wrong?

writing a code with error handling in mind, unexpected errror to handle.


# Value Error - try, except

```python
try:
    x = int(input("What's x?: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")
```
# If you dont know whats going on?

what can go wrong will go wrong...

# Name Error

it happens in peace of code before it executes.

# 'else' 

You can use 'else' also in execptions as in conditionals. 

```python
try:
    x = int(input("What's x?: "))  
except ValueError:
    print("x is not an interger")

else:
    print(f"x is {x}")
```

# Using a loop

you can loop the question till user inputs correct input and breaks out of the loop

```python
while True:
    try:
        x = int(input("What's x?: "))  
    except ValueError:
        print("x is not an interger")
    else:
        break
        
print(f"x is {x}")
```
# Break

 you can break out of from the loop or conditionals like 'if' or 'else'. return function is stronger than break function

 ```python
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
```

# Pass

if you want to pass on doing anything with it so you want to catch it. Or it ignores code and passes it.

## wtf if indentation

# Debugging

solving you problem when your code is shit. what kind of tools we have to chase down the bugs you wrote in your code.

using 'print()' is your friend to debugging your code and figure out what is wrong.

```python
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid (n):
    for i in range(n):
        print(i, end=" ")  # this is where print used to debugg why it isnt starts with 0
        print("#" * i)

if __name__ == "__main__":
    main()
```

## Breakpoints


