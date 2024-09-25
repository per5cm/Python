import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_format = re.search(r"^(\d\d?):?(\d?\d?) ([AP]M) to (\d\d?):?(\d?\d?) ([AP]M)", s)
    if not time_format:
        raise ValueError
    
    start_hour, start_minute, start_am_pm, end_hour, end_minute, end_am_pm = time_format.groups()
    
    # Default minutes to "00" if not provided
    start_minute = "00" if start_minute == "" else start_minute
    end_minute = "00" if end_minute == "" else end_minute
    
    # Convert minutes to integers and validate them
    if int(start_minute) >= 60 or int(end_minute) >= 60:
        raise ValueError("Invalid minutes.")

    start_hour = int(start_hour)
    if start_am_pm == "PM" and start_hour != 12:
        start_hour += 12
    elif start_am_pm == "AM" and start_hour == 12:
        start_hour = 0

    end_hour = int(end_hour)
    if end_am_pm == "PM" and end_hour != 12:
        end_hour += 12
    elif end_am_pm == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"


if __name__ == "__main__":
    main()





            



