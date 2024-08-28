def main():
    while True:
        try:
            fraction = input("\nFraction: ")
            x, y = fraction.split("/")
            x = int (x)
            y = int (y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = (x / y) * 100

            if percentage <= 1:
                print("\nE\n")
            elif percentage >= 99:
                print("\nF\n")
            else:
                print(f"\n{round(percentage)}%\n")
            break
        
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()

