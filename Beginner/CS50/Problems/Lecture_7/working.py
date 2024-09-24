import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_format = re.search(r"^(\d\d?):(\d\d?)\s*([AP]M)\s*to\s*(\d\d?):(\d\d?)\s*([AP]M)", s)
    if not time_format:
        return "Invalid format"
    
    hour, minute, am_pm = time_format.groups()
    hour = int(hour)

    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()
