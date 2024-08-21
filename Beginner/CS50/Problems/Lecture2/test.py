def main():
    coke_price = 50  # The price of a Coke is fixed at 50 cents.
    coke_coin = [1, 2, 5, 10, 20, 25, 30, 35, 40, 45]  # Valid coin denominations

    while coke_price > 0:
        print(f"Amount Due: {coke_price}")
        coin = int(input("Insert Coin: "))
        
        if coin in coke_coin:
            coke_price -= coin
        else:
            print("Invalid coin. Please insert a valid coin.")

    if coke_price == 0:
        print("Change Owed: 0")
    else:
        print(f"Change Owed: {-coke_price}")

main()

    
