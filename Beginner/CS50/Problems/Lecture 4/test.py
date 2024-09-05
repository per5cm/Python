import random

def askNum():
  while(1):
    try:
      userInput = int(input("Enter a number: "))
      break
    except ValueError:
      print("Incorrect Input!")

  return userInput

def askQuestion():

  x = random.randint(1, 100)
  y = random.randint(1, 100)

  print("What is " + str(x) + " + " + str(y))

  u = askNum()

  if (u == x + y):
    return 1
  else:
    return 0

amount = 10
correct = 0
for i in range(amount):
  correct += askQuestion()

print("You got %d correct out of %d" % (correct, amount))