def main():
    menu_dict = { 
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    order_list = []  # Initialize empty list to store the prices of the items user enters
    order_total = 0.0  # Initialize order total

    while True:
        try:
            item = input("Item: ").strip().title()
            
            if item in menu_dict:
                order_list.append(menu_dict[item])  # Append the price of the item to list
                order_total = sum(order_list)
                print(f"Total: ${order_total:.2f}")
            else:
                # If item is not on the menu, print error and re-prompt user
                print("Item not found on menu.")
                
        except EOFError:
            print(f"Final Total: ${order_total:.2f}")
            break

if __name__ == "__main__":
    main()
