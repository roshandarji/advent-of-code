from icecream import ic
import re


class Card: # Set up class to handle individual cards
    def __init__(self, index: int, win: list, numbers: list) -> None:
        self.index = index
        self.win = win
        self.numbers = numbers

    @classmethod
    def from_string(cls, card_string): # Method to parse cards from string
        index = (
            int(re.search(r"Card\s*(\d+):", card_string.strip()).group(1))
            if re.search(r"Card\s*(\d+):", card_string)
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


# Day 4 input
card_set = read_cards(r"2023/day-4/d4p1-input.txt")
n = {card_num: 1 for card_num in range(1, len(card_set) + 1)}
for card in range(len(card_set)):
    matches = len(set(card_set[card].win) & set(card_set[card].numbers))
    
    for copies in range(card_set[card].index, card_set[card].index + matches):
        n[copies] += n[card_set[card].index]

ic(sum(n.values()))