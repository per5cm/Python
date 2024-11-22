import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")

            if tries == 3:
                print(f"Correct answer is: {x + y}")

    print(f"Final score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                print(f"Selected level {level}.")
                return level
        except ValueError:
            continue
        print("\nInvalid input\n")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("\nInvalid level\n")

if __name__ == "__main__":
    main()
