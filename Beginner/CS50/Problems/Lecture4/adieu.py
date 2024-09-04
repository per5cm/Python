import inflect

def main():

    inflect_engine = inflect.engine()
    name_family_list = []

    while True:
        try:
            names = input("Name: ").strip().title()
            name_family_list.append(names)

        except EOFError:
            print("Adieu, adieu, to", inflect_engine.join(name_family_list))
            break

if __name__ == "__main__":
    main()
