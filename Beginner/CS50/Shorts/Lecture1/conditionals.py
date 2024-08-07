def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")
    if diffculty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        print("Enter a valid number of players")
        
    
    
def recommend(game):
    print ("You might like", game)
    
    
main()