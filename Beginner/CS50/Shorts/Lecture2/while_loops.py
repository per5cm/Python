## While loop is perfect choice when you want to keep looping while some cindition is ture, 
## but your not exactly sure how long you're going to loop at the end of the day.

from soil import sample  # Imports the sample function from the soil module

def main():
    moisture = sample()  # Gets the initial moisture level
    days = 0  # Initializes the day counter
    print(f"Moisture is {moisture}%")  # Prints the initial moisture level

    while moisture > 20:  # Checks if moisture is greater than 20%
        moisture = sample()  # Samples the moisture level again
        days += 1  # Increments the day counter
        print(f"Day {days}: Moisture is {moisture}%")  # Prints the moisture level and day count

    print("Time to water!")  # Indicates it's time to water the plants

main()  # Calls the main function to run the program
