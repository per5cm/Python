def main():
    x = int(input("What's x?: "))
    print("x squared is: ", square(x))

def square(n):
    return n + n # test will show that i need to change * multiplication instead of + plus.

if __name__ == "__main__":
    main()

## Second Version without interger

def main():
    x = input("What's x?: ")
    print("x squared is: ", square(x))

def square(n):
    return n + n # test will show that i need to change * multiplication instead of + plus.

if __name__ == "__main__":
    main()