from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

available_fonts = figlet.getFonts()

text_input = input("Text Input: ")


if len(sys.argv) == 1:
    fonts = random.choice(available_fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
else:
    sys.exit(1)
figlet.setFont(font=font)

print(figlet.renderText(text_input))

