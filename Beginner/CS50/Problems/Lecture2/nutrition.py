fruits = {
    "apple": "130", "avocado": "50",
    "sweet cherries": "100", "kiwifruit": "90",
    "pear": "100"
}

nutrition = input("Item: ").lower()
if nutrition in fruits:
   print(fruits[nutrition])


    