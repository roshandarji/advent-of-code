# Title:    2023 Advent of Code -- Day 1 Part 1: Trebuchet?!
# Author:   Roshan Darji
# Date:     2023-12-09

import numpy as np

def parse_string(string):
    # Extract first and last digit from string
    first_digit = next(char for char in string if char.isdigit())
    last_digit = next(char for char in reversed(string) if char.isdigit())

    # Concatenate and return digits as integer
    return int(first_digit + last_digit)

# Tests for parse_string
assert parse_string("abc123") == 13
assert parse_string("abc123def456") == 16
assert parse_string("1abc2") == 12
assert parse_string("pqr3stu8vwx") == 38
assert parse_string("a1b2c3d4e5f") == 15
assert parse_string("treb7uchet") == 77

# Read input file
with open("day-1/d1p1-input.txt", "r") as f:
    input = f.read().splitlines()

# Parse input file
input = np.array([parse_string(string) for string in input])

# Sum all integers in input
print(np.sum(input))


