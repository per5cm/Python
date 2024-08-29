from datetime import datetime

while True:
    date_input = input("Date: ").strip()
    
    try:
        if "/" in date_input:
            date = datetime.strptime(date_input, "%m/%d/%Y")
            output = date.strftime("%m-%d-%Y")
        elif " " in date_input and "," not in date_input:
            date = datetime.strptime(date_input, "%B %d %Y")
            output = date.strftime("%B %d, %Y")
        else:
            raise ValueError("Incorrect format")

        print(output)
        break
    
    except ValueError:
        print("Please try again.")


