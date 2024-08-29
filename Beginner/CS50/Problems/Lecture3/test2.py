from datetime import datetime

while True:

    date_input = input("Date: ")

    try:
        if "/" in date_input:
            date = datetime.strptime(date_input, "%Y/%m/%d")
            output = date.strftime("%Y-%m-%d")
        elif " " in date_input and "," not in date_input:
            date = datetime.strptime(date_input, "%B %d %Y")
            output = date.strftime("%B %d, %Y")

        print(output)
        break

    except ValueError:
        print("Try again: ")