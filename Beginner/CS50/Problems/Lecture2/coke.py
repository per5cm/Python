def main():
    coke_price = 50

    while coke_price > 0:
        print(f"Amount Due: {coke_price}\n")
        coke_coin = int(input("Insert Coin: "))
        if coke_coin in [5, 10, 25]:
            coke_price -= coke_coin
        if coke_price <= 0:
            print(f"Change Owed: {-coke_price}\n")

main()