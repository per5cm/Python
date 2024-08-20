## While loop is perfect choice when you want to keep looping while some cindition is ture, but your not exactly sure how long you're going to loop at the end of the day.

from soil import sample


def main():
    moisture = sample()
    days = 0
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")


main()