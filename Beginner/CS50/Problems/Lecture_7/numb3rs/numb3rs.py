import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(pattern, ip):
        parts = ip.split(".")
        for part in parts:
            if not (0 <= int(part) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
