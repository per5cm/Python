## Initial version for validating email address.

email = input("Wha's your email? ").strip()

username, domain = email.split("@") # defined two variables at once

if username and domain.endswith("edu"):
    print("Valid")
else:
    print("Invalid")

## Version with re.search(pattern, string, flags=0)

import re

email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # or (".+@.+", email) or ("..*@..*, email") # \ special sequence that reads .edu # [^@] means anything but @ sign 
    # print("Valid")
if re.search(r"^(\w|\.)+@(\w\.)?\w+\.(edu | com | de | gov | eu)$", email, re.IGNORECASE): # (\w\s)+@ # you can also (email.lower())
    print("Valid")
else:
    print("Invalid")

