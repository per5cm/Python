## Initial version.

url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/", "") # url.replace("...")
print(f"Username: {username}")

## With re liabrary re.sub(pattern, string, count=0, flags=0)

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

## Next Version

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # when you start in perenteceese (?:) its non- capturing or you say tolerate both or a string input.
    print(f"Username: ", matches.group(1))

