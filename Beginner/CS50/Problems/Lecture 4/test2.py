from pyfiglet import Figlet
import sys
import random

# Initialize Figlet object
figlet = Figlet()

# Get the list of available fonts
available_fonts = figlet.getFonts()

# Read input text
text_input = input("Text Input: ")

# Determine the font to use
font = None  # Initialize font variable

if len(sys.argv) == 1:
    # No command-line arguments, choose a random font
    font = random.choice(available_fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # Command-line argument specifies a font
    font = sys.argv[2]
    if font not in available_fonts:
        # Font not found in available fonts
        print(f"Error: Font '{font}' not found.")
        sys.exit(1)
else:
    # Invalid command-line arguments
    print("Usage: python script.py [-f | --font FONT_NAME]")
    sys.exit(1)

# Set the font and render the text
try:
    figlet.setFont(font=font)
    rendered_text = figlet.renderText(text_input)
    print(rendered_text)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
