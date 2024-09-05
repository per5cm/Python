import random

lower_bound = 1
upper_bound = 100

secret_number = random.randint(lower_bound, upper_bound)

def main():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if guess == secret_number:
                print("Just right!", guess)
                break
            elif guess < secret_number:
                print("Too small!", guess)
            elif guess > secret_number:
                print("Too large!", guess)
            else:
                print()

        except ValueError:
            continue
        except EOFError:
            break