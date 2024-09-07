from pyfiglet import Figlet
import sys

figlet = Figlet()

try:
    if len(sys.argv) == 1:
        font_is = True
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_is = False
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("\nInvalid font:\n")
        else:
            figlet.setFont(font=font)
    else:
        sys.exit()
except:
    print("Invalid usage")
    sys.exit(1)

text_input = input("Text input: ").strip()

print("Output:","\n", figlet.renderText(text_input))
