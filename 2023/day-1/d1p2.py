# Title:    2023 Advent of Code -- Day 1 Part 2: Trebuchet?!
# Author:   Roshan Darji
# Date:     2023-12-09

import numpy as np


def replace_numbers_with_words(string: str):
    # Define a dictionary to map spelled-out digits to their corresponding numerical values
    digit_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # Replace all digits in string with their spelled-out counterparts
    for word, digit in digit_mapping.items():
        string = string.replace(str(digit), word)
    
    return string


def substring_with_indices(string: str):
    # Define a dictionary to map spelled-out digits to their corresponding numerical values
    digit_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    substring_with_indices = []

    # Find all substrings in string that are spelled-out digits
    for word in digit_mapping.keys():
        index = string.find(word)
        while index != -1:
            substring_with_indices.append((word, index))
            index = string.find(word, index + 1)

    # Sort substrings by index
    substring_with_indices.sort(key=lambda x: x[1])

    # Extract translated digits from substrings
    substring_translated = [
        digit_mapping[word] for word, index in substring_with_indices
    ]

    return substring_translated


def parse_string(string: str):
    string = replace_numbers_with_words(string)
    substrings = substring_with_indices(string)

    # Extract first and last digit from string
    first_digit = substrings[0]
    last_digit = substrings[-1]

    # Concatenate and return digits as integer
    return int(str(first_digit) + str(last_digit))


# Tests for parse_string
assert parse_string("two1nine") == 29

# Read input file
with open("day-1/d1p2-input.txt", "r") as f:
    input = f.read().splitlines()

# Parse input file
input = np.array([parse_string(string) for string in input])

# Sum all integers in input
print(np.sum(input))
