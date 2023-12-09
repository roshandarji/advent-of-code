# Title:    2023 Advent of Code -- Day 2 Part 1: Cube Conundrum
# Author:   Roshan Darji
# Date:     2023-12-09

import re
from icecream import ic


def extract_cube_counts(string: str) -> dict:
    output = {"game": [], "red": [], "blue": [], "green": []}

    # Extract game number
    game = re.search(r"Game (\d+)", string).group(1)
    output["game"] = int(game)

    # Extract cube counts
    cubes = re.findall(r"(\d+) (\w+)", string)

    # Extract red, blue, and green cubes
    output["red"] = max([int(count) for count, color in cubes if color == "red"])
    output["blue"] = max([int(count) for count, color in cubes if color == "blue"])
    output["green"] = max([int(count) for count, color in cubes if color == "green"])

    return output


# Tests for extract_cube_counts
assert extract_cube_counts(
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
) == {"game": 1, "red": 4, "blue": 6, "green": 2}
assert extract_cube_counts(
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
) == {"game": 2, "red": 1, "blue": 4, "green": 3}
assert extract_cube_counts(
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
) == {"game": 3, "red": 20, "blue": 6, "green": 13}
assert extract_cube_counts(
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
) == {"game": 4, "red": 14, "blue": 15, "green": 3}
assert extract_cube_counts(
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
) == {"game": 5, "red": 6, "blue": 2, "green": 3}


with open("day-2/d2p1-input.txt", "r") as file:
    lines = file.readlines()

# Extract cube counts from each game
cube_counts = [extract_cube_counts(line) for line in lines]

# Set maximum number of cubes of each type for a valid game
max_red = 12
max_green = 13
max_blue = 14

# Filter out invalid games
valid_games = [
    game
    for game in cube_counts
    if game["red"] <= max_red
    and game["green"] <= max_green
    and game["blue"] <= max_blue
]

# Sum the game numbers of all valid games
result = sum([game["game"] for game in valid_games])
ic(result)
