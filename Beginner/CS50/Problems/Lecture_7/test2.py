import re

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("Invalid input")

def convert(s):
    # Validate input format using a better regex pattern
    pattern = r"(\d{1,2}(:\d{2})?) ([AP]M) to (\d{1,2}(:\d{2})?) ([AP]M)"
    match = re.match(pattern, s)
    if not match:
        raise ValueError
    # Extract time components
    time = match.groups()
    first_time = newFormat(time[0], time[2])
    second_time = newFormat(time[3], time[5])
    return first_time + ' to ' + second_time

def newFormat(time, am_pm):
    if ':' in time:
        hour, minute = map(int, time.split(':'))
    else:
        hour = int(time)
        minute = 0

    if hour > 12 or hour < 1 or minute >= 60:
        raise ValueError

    if am_pm == 'PM' and hour != 12:
        hour += 12
    elif am_pm == 'AM' and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":

    main