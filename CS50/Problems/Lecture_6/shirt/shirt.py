import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_path, output_path = sys.argv[1:3]
valid_extensions = {".jpg", ".png", ".jpeg"}
input_ext, output_ext = map(lambda x: os.path.splitext(x)[1].lower(), [input_path, output_path])

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid file format!")
elif input_ext != output_ext:
    sys.exit("Mismatched input/ output formats!")

try:
    input_image = Image.open(input_path)
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("File does not exist")

else:
    # Resize the input image to match the size of the shirt image
    input_image = ImageOps.fit(input_image, shirt.size)
    # Paste the shirt image on top of the resized input image
    input_image.paste(shirt, (0, 0), shirt)
    # Save the result
    input_image.save(output_path)
