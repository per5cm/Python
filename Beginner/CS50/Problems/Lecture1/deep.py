deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

if deep.strip() == "42":
    print("Yes")
elif deep.lower() == "forty-two":
    print("Yes")
elif deep.lower() == "forty two":
    print("Yes")
else:
    print("No")
