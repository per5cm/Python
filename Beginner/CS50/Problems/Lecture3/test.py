def main():
    while True:
        try:
            # Prompt the user for input
            fraction = input("Fraction: ")
            # Split the input into numerator and denominator
            x, y = fraction.split("/")
            # Convert the inputs into integers
            x = int(x)
            y = int(y)
            # Check for invalid cases
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            # Calculate the percentage
            percentage = (x / y) * 100

            # Output the appropriate message
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                # Round the percentage to the nearest integer
                print(f"{round(percentage)}%")
            break  # Exit the loop if everything is valid

        except (ValueError, ZeroDivisionError):
            # If there's an error, prompt the user to enter a valid fraction
            pass


if __name__ == "__main__":
    main()
