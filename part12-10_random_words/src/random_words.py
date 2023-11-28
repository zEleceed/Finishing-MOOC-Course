import random


def word_generator(characters: str, length: int, amount: int):
    for letter in range(amount):
        yield "".join(random.choice(characters) for letter in range(length))
