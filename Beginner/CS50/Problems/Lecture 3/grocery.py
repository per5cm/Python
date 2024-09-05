def main():
    grocery_list = ["mango", "strawberry", "milk", "sweet potato", "tortilla"]

    user_input = 0
    item_count = {}

    while True:
        try:
            grocery_item = input("Input: ")
            grocery_list.append(grocery_item)
            user_input += 1

            if grocery_item in item_count:
                item_count[grocery_item] += 1
            else:
                item_count[grocery_item] = 1

        except EOFError:
            #print(f"{item_count}")
            break
    for item, count in item_count.items():
        print(f"{count} {item}")

if __name__ == "__main__":
    main()

