#guess = 10 
#print (guess)

#Function
#def get_guess():
#    guess = 10
#    return guess 

#print(get_guess())

#Function input
#def get_guess():
#    guess = input("Enter a guess: ")
#    return guess
#
#def main ():
#    guess = get_guess()
#    print(guess)
#
#main()

def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main ():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

main()