from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        #print(img.size)
        #print(img.format)
        img = img.rotate(180)
        img.filter(ImageFilter.BLUR) #blur filter
        img.filter(ImageFilter.FIND_EDGES) # an other fun filter
        img.save("out.jpeg")

main()