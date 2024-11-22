import re
import sys


def main():  
    print(convert(input("Hours: ")))

def convert(s):
    time_format = re.match(r"^(\d\d?):?(\d?\d?) ([AP]M) to (\d\d?):?(\d?\d?) ([AP]M)", s)
    if not time_format:
        raise ValueError
    
    start_hour, start_minute, start_am_pm, end_hour, end_minute, end_am_pm = time_format.groups()

    start_hour, end_hour = int(start_hour), int(end_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    if not (1 <= start_hour <= 12 and 0 <= start_minute <= 59 and 1 <= end_hour <= 12 and 0 <= end_minute <= 59):
        raise ValueError
    
    start_hour = convert_hour(start_hour, start_am_pm)
    end_hour = convert_hour(end_hour, end_am_pm)

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

def convert_hour(hour, am_pm):    
    if am_pm == "PM" and hour != 12:
        return hour + 12
    elif am_pm == "AM" and hour == 12:
        return 0
    return hour


if __name__ == "__main__":
    main()
