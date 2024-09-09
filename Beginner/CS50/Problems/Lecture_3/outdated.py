from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:

    date_input = input("Date: ").strip()

    try:
        if "/" in date_input:
            date = datetime.strptime(date_input, "%m/%d/%Y")
        else:
            if any(month in date_input for month in months):
                date = datetime.strptime(date_input, "%B %d, %Y")

        print(date.strftime("%Y-%m-%d"))
        break

    except ValueError:
        print("Try again: ")


