## Initial Version

import random

card = ["jack", "queen", "king"]


def main():
    print(random.choice(card))

main()

## Second Version draws two cards

import random

card = ["jack", "queen", "king"]


def main():
    print(random.choice(card, k=2))

main()

## Using sample will draw without replacment card.

import random

card = ["jack", "queen", "king"]


def main():
    print(random.sample(card, k=2))

main()

## To ajust parameters to your favor

import random

card = ["jack", "queen", "king"]


def main():
    print(random.choice(card, weights=[75, 20, 5], k=2))

main()

## Hard to debugg randomness. useing 'seed' for debugg randomness.

import random

card = ["jack", "queen", "king"]


def main():
    random.seed(0)
    print(random.choice(card, k=2))

main()