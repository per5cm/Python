import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the first row as headers
            print(tabulate(reader, headers=header, tablefmt="grid"))  # Directly pass the reader object
    except FileNotFoundError:
        sys.exit("File does not exist")
