import sys

check_list = []

# Argument count Check:
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# File extension check.
elif not sys.argv[1].endswith(".py"):
    sys.exit("Is not Python file")

# File reading and Filtering:
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if not line.isspace() and not line.strip().startswith("#"):
                    check_list.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

# Final Output: if file is python file it will read and print result.
    else:
        print(len(check_list))

    

