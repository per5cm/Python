## Initial Version

def hello():
    print("hello,")

name = input("What's your name? ")
hello()
print(name)


## Second Version

def hello(to):
    print("hello,", to)
    
name = input ("What's your name? ")
hello(name)

## More Polite Version

def hello(to="world"):
    print("hello,", to)
    
hello()
name = input("What's your name? ")
hello(name)

## Main method

def main():
    name = input("What's your name? ")
    hello(name)
   
    
def hello(to="world"):
    print("hello,", to)
 
    
main()

## Scope (wtf is scope)

def main():
    name = input("What's your name? ")
    hello()
    
def hello(to="world"): ## Technicaly hello function different name, callde'to', or name its own arguments.
    print("hello,", to)
    
main()