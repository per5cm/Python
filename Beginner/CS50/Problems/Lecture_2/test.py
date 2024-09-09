def main():
    character = letter(input("Input: "))
    character = letter(character)
    print("Output: ", character)

def letter(string):
    for char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        string = string.replace(char, "")
    return string

if __name__ == "__main":
    main()