import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for number in matches.groups():
            if int(number) > 255:
                return False
            return True


if __name__ == "__main__":
    main()
