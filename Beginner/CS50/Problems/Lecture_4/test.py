def main():
    while True:
        try:
            fraction_input = input("\nFraction: ")
            percentage = fraction(fraction_input)
            gouge(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass


def fraction(fraction_input):
    x, y = fraction_input.split("/")
    x = int (x)
    y = int (y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return (x / y) * 100

def gouge(percentage):
    if percentage <= 1:
        print("\nE\n")
    elif percentage >= 99:
        print("\nF\n")
    else:
        print(f"\n{round(percentage)}%\n")

if __name__ == "__main__":
    main()
