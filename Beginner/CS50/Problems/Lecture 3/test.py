from datetime import datetime

while True:
    # Prompt user for input
    date_input = input("Date: ").strip()
    
    try:
        # Try to parse the date in MM/DD/YYYY format
        if "/" in date_input:
            date = datetime.strptime(date_input, "%m/%d/%Y")
        
        if "," in date_input:
            date = datetime.strptime("%B %m, %Y")

        elif " " in date_input and "," not in date_input:
            date = datetime.strptime(date_input, "%B %d %Y")
            print(date.strftime("%B %m, %Y"))
            break
        # Try to parse the date in Month Day, Year format
        #else:
            #date = datetime.strptime(date_input, "%B %d %Y")
        
        # Output the date in YYYY-MM-DD format
        print(date.strftime("%Y-%m-%d"))
        break  
    
    except ValueError:
        print("Invalid date format. Please try again.")


