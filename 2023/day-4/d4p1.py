from icecream import ic
import re
import time

class Card: # Set up class to handle individual cards
    def __init__(self, index: int, win: list, numbers: list) -> None:
        self.index = index
        self.win = win
        self.numbers = numbers

    def calculate_points(self) -> int:
        n = 0
        for i in self.numbers:
            n += 1 if i in self.win else 0

        return 2 ** (n - 1) if n > 0 else 0

    @classmethod
    def from_string(cls, card_string): # Method to parse cards from string
        index = (
            int(re.search(r"Card (\d+):", card_string).group(1))
            if re.search(r"Card (\d+):", card_string)
            else None
        )
        _, remainder = card_string.split(":", 1)
        win, numbers = re.split(r"\|", remainder.strip())
        win = [int(num) for num in win.split()]
        numbers = [int(num) for num in numbers.split()]

        return cls(index, win, numbers)

def read_cards(filename: str) -> list: # Read in cards from input file
    cards = []
    with open(filename, "r") as f:
        for _, line in enumerate(f):
            card = Card.from_string(line.strip())
            cards.append(card)

    return cards

# Unit tests
example_card_set = read_cards(r"2023/day-4/d4p1-example.txt")
assert example_card_set[0].index == 1, "Index doesn't match"
assert example_card_set[0].win == [41, 48, 83, 86, 17], "Win numbers don't match"
assert example_card_set[0].numbers == [83, 86, 6, 31, 17, 9, 48, 53], "Card numbers don't match"
assert example_card_set[0].calculate_points() == 8, "Individual point calculation is incorrect"

total_points = 0
for card in example_card_set:
    total_points += card.calculate_points()

assert total_points == 13, "Total point calculation is incorrect"

# Day 4 input
card_set = read_cards(r"2023/day-4/d4p1-input.txt")
total_points = 0

for card in card_set:
    total_points += card.calculate_points()

ic(total_points)