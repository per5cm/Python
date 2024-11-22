def main():
    character = shorten(input("Input: "))
    print("Output: ", character)

def shorten(word):
    for char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()