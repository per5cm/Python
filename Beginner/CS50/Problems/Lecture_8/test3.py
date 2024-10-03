import sys
import inflect
from datetime import date

class Date:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        self.p = inflect.engine()
        
    def calculate_age(self):
        try:
            year, month, day = self.date_of_birth.split("-")
            birth = date(int(year), int(month), int(day))
        except:
            sys.exit("Invalid date")
            
            
        dif = date.today() - birth
        letters = self.p.number_to_words(int(dif.total_seconds() / 60), andword="")
        return f"{letters.capitalize()} minutes"
    
def main():
    date_of_birth = input("Date of Birth: ")
    age_in_minutes = Date(date_of_birth)
    print(age_in_minutes.calculate_age())
    
if __name__ == "__main__":
    main()