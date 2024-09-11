def main():  
    fraction_input = input("\nFraction: ")
    percentage = fraction(fraction_input)
    result = gauge(percentage)
    print(result)
        


def fraction(fraction_input):
    x, y = fraction_input.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = (x / y) * 100
    return round(percentage)  


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

