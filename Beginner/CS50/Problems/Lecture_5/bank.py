def main():

    greeting = input("Enter your greeting: ") #.strip().lower()
    print_value = value(greeting)
    print(f"${print_value}")

def value(greeting):
    if "hello" == greeting:
        return 0
    elif "h" == greeting:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()