from pyfiglet import Figlet
import sys

figlet = Figlet()
try:
    if len(sys.argv) == 1:
        is_Font = True
    elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '--font':
        is_Font = False
    if is_Font == False:
        figlet.setFont(font=sys.argv[2])
except:
    print("Invalid usage")
    sys.exit(1)

figlet.getFonts()

prompt = input("Input: ")
print("Output:",'\n', figlet.renderText(prompt))