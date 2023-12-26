from icecream import ic
from typing import Generator, Tuple, List
import re

def read_input(filename: str) -> list:
    with open(filename, 'r') as f:
        return f.read().splitlines()

def is_symbol(char: str) -> bool:
    return char != '.' and not char.isdigit()

def get_part_numbers(input: list) -> Generator[Tuple[int, str, int, int, int], None, None]:
    for i, line in enumerate(input):
        for match_num in re.finditer(r'\d+', line):
            start = match_num.start(0) - 1
            end = match_num.end(0)
            number = int(match_num.group(0))
            yield i, line, start, end, number

schematic = read_input("2023/day-3/d3p1-input.txt")
part_sum = 0

for i, line, start, end, number in get_part_numbers(schematic):
    # Check if a symbol is to the left or right of a number
    if (start >= 0 and is_symbol(line[start])) or (end < len(line) and is_symbol(line[end])):
        part_sum += number
    
    # Check if a symbol is in the lines above or below the number
    for j in range(start, end + 1):
        if j >= len(line): # Check if we're at the end of the line first
            continue
        if (i > 0 and is_symbol(schematic[i - 1][j])) or (i < len(schematic) - 2 and is_symbol(schematic[i + 1][j])):
            part_sum += number

ic(part_sum)