# initial program

## x = int(input("What's x? "))

## if x % 2 == 0:
##     print("Even")
## else:
##     print("Odd")

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):         # shorter version
    if n % 2 == 0:      ## return True if n % 2 == 0 else False
        return True
    else:               # pythonic way
        return False    ## return (n % 2 == 0) <--what happens in parentheses will happen first.
        
main()