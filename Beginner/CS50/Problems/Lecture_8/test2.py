import sys
import inflect
from datetime import date

date_of_birth = input("Date of Birth: ")
p = inflect.engine()

def main():
    try:
        x, y, z = date_of_birth.split("-")
        birth = date(int(x), int(y), int(z))
    except:
        sys.exit("Invalid date!")

   
    dif = date.today() - birth
    letters = p.number_to_words(int(dif.total_seconds() / 60), andword="")
    print(f"{letters.capitalize()} minutes")

if __name__ == "__main__":
    main()

