## Initial Version

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

## With expressions.

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # := valrus operator
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")