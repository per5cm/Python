def main():
    # Prompt the user for fuel input and display the corresponding gauge
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        # Split the input fraction string and convert X and Y to integers
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        # Raise errors for invalid input
        if y == 0:
            raise ZeroDivisionError("Y cannot be zero.")
        if x > y:
            raise ValueError("X cannot be greater than Y.")

        # Calculate the percentage and round it to the nearest integer
        percentage = round((x / y) * 100)
        return percentage

    except ValueError:
        raise ValueError("Invalid input. X and Y must be integers.")


def gauge(percentage):
    # Return corresponding gauge values based on the percentage
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
