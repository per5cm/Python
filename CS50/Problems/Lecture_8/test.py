import inflect
from datetime import date

class Date:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)
        
    def date_to_words(self):
        p = inflect.engine()
        return f"{p.number_to_words(self.date.day)}{self.date.strftime('%B')}{self.date.year}"
        

def main():
    try:
        year, month, day = map(int(input("Enter your Birthdate: "))).split("-")
        print(f"{Date(year, month, day).to_words()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
