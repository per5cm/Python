from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

available_fonts = figlet.getFonts()
f = random.choice(available_fonts)

figlet.setFont(font=f)

s = input("Text Input: ")
if len(sys.argv) < 1 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    print(available_fonts)
elif s == 0:
    sys.exit() 
print(figlet.renderText(s))