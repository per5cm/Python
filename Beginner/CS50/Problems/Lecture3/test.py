from datetime import datetime

# List of valid month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Prompt user for input
    date_input = input("Date: ").strip()
    
    try:
        # Try to parse the date in MM/DD/YYYY format
        if "/" in date_input:
            date = datetime.strptime(date_input, "%m/%d/%Y")
            print(date)
        
        # Try to parse the date in Month Day, Year format
        else:
            date = datetime.strptime(date_input, "%B %d %Y")
            
        
        # Output the date in YYYY-MM-DD format
            print(date.strftime("%Y-%m-%d"))
            break  # Exit loop on successful parsing
    
    except ValueError:
        # If date parsing fails, prompt the user to try again
        print("Invalid date format. Please try again.")

