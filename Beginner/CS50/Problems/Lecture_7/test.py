import re
import sys


count = (input("Text: "))

if re.search(r"\bum\b", count):
    print("matched!")
else:
    print("not matched!")
            



