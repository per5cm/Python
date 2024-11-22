expression = input("Expression: ").strip()

x, y, z = expression.split()

x = int(x)
z = int(z)

match y:
    case "+":
        print(f"{x + z:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "/":
        print(f"{x / z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
    case _:
        print("Try again!")


## interpreter.py

# Step 1: Prompt the user for an arithmetic expression

expression = input("Enter an arithmetic expression (x y z): ")

# Step 2: Parse the input into three parts

x, y, z = expression.split()

# Convert x and z to integers

x = int(x)
z = int(z)

# Step 3: Perform the calculation based on the operator

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z

# Step 4: Output the result as a floating-point value formatted to one decimal place

print(f"{result:.1f}")

## eval

x=input("what's x? ")


result=float(eval(x))

print(result)
