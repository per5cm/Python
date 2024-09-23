import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="(https?://)?(www\.)?youtube\.com/embed/(?P<embed>[\w-]+)"', s)
    if match: 
        embed = match.group("embed")
        return f"https://youtu.be/{embed}"
    return None



if __name__ == "__main__":
    main()
