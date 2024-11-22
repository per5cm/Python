def main():

    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x_new = int(x)
            y_new = int(y)
            f = x_new / y_new
            if f <= 1:
                p = round(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()