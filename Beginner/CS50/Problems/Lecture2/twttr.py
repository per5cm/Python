def main():
    character = letter(input("Input: "))
    print("Output: ", character)

def letter(string):
    for char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        string = string.replace(char, "")
    return string

main()