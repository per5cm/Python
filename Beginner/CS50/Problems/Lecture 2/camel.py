camelCase = input("camelCase: ")
snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print("snake_case: ", snake_case)
