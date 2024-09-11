def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check lenght
    if len(plate) < 2 or len(plate) > 6:
        return False
    # First characters must be letters
    if not (plate[:2].isalpha()):
        return False
    # All characters must be alphanumeric
    if not plate.isalnum():
        return False
    # Check the transition between letters and numbers
    for item in range(len(plate)-1):
        if plate[item].isdigit() and plate[item + 1].isalpha():
            return False
    # If there are digits, they must not start with '0'
    for item in plate:
        if item.isdigit():
            return item != '0'
    else:
        return True


main()