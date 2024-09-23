import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'src="(?:https?://(?:www\.)?)?youtube\.com/embed/(?P<vid_id>[^"]+)"', s)
    if match:
        vid_id = match.group("vid_id")
        return f"https://youtu.be/{vid_id}"
    return None


if __name__ == "__main__":

    main()