import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Correct the regex to match "AM" and "PM"
    time_format = re.search(r"^(\d\d?):(\d\d)\s*([AP]M)\s*to\s*(\d\d?):(\d\d)\s*([AP]M)", s)
    if not time_format:
        return "Invalid format"
    
    # Unpack all 6 values (start hour, minute, AM/PM, end hour, minute, AM/PM)
    start_hour, start_minute, start_am_pm, end_hour, end_minute, end_am_pm = time_format.groups()
    
    # Convert start time
    start_hour = int(start_hour)
    if start_am_pm == "PM" and start_hour != 12:
        start_hour += 12
    elif start_am_pm == "AM" and start_hour == 12:
        start_hour = 0

    # Convert end time
    end_hour = int(end_hour)
    if end_am_pm == "PM" and end_hour != 12:
        end_hour += 12
    elif end_am_pm == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"


if __name__ == "__main__":
    main()



            



