def is_valid(s):
    # Check if the plate starts with at least two letters
    if not (s[:2].isalpha()):
        return False

    # Check the length of the plate
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if numbers are only at the end and the first number is not '0'
    if any(char.isdigit() for char in s):
        for i in range(len(s)):
            if s[i].isdigit():
                # Check if a digit appears before this digit
                if not s[i:].isdigit():
                    return False
                # Check if the first number is '0'
                if s[i] == '0':
                    return False
                break

    # Ensure there are no periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    # If all checks pass, return True
    return True

def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
