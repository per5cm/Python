import random

coin = random.choice(["heads", "tails"])
print (coin)

## Alternative version using 'from' keyword.

from random import choice

coin = random.choice(["heads", "tails"])
print(coin)

## Alternative version with randit version

import random
number = random.randint(1, 10)
print(number)

## Alternative version with .shuffle.

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(cards)
