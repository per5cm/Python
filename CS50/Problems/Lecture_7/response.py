from validator_collection import validators, checkers, errors

def main():
    email_input = input("What's your e-mail address?: ")
    try:
        validators.email(email_input)
        print("Valid")
    except:
        print("Invalid") 


if __name__ == "__main__":
    main()