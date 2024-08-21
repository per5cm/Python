def main():
    coke_price = 50
    amount_due = coke_price

    while amount_due > 0:
        print(f"Amount Due: {amount_due} cents")
        coke_coin = float(input("Insert Coin (accepted: 5, 10, 25): "))

        if coke_coin in [5, 10, 25]:
            amount_due -= coke_coin
        else:
            print("Invalid coin. Please insert a coin of value 5, 10, or 25 cents.")

    if amount_due < 0:
        print(f"Change Owed: {-amount_due} cents")
    else:
        print("Exact amount received. No change owed.")

if __name__ == "__main__":
    main()

