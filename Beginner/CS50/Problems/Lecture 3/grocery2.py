def main():
    item_count = {}

    while True:
        try:
            grocery_item = input("Input: ")

            if grocery_item in item_count:
                item_count[grocery_item] += 1
            else:
                item_count[grocery_item] = 1

        except EOFError:
            for item in sorted(item_count.keys()):
                print(item_count[item], item.upper())
            break

if __name__ == "__main__":
    main()
