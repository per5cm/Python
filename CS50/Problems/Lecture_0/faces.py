def main():
    smiley = input("Input your smiley face: ")
    smiley = convert(smiley)
    print(smiley)


def convert(smiley):
    smiley = smiley.replace(":)", "🙂")
    smiley = smiley.replace(":(", "🙁")
    return smiley

main()
