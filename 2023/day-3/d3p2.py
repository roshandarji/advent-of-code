from icecream import ic
from typing import Generator, Tuple, List
import re


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def is_symbol(char: str) -> bool:
    return char != "." and not char.isdigit()


def get_parts(input: list) -> List[Tuple[int, str, List[Tuple[int, int, int]]]]:
    parts = []
    for i, line in enumerate(input):
        parts.append((i, line, []))
        for match_num in re.finditer(r"\d+", line):
            start = match_num.start(0) - 1
            end = match_num.end(0)
            number = int(match_num.group(0))
            part = (start, end, number)
            parts[i][2].append(part)

    return parts

def solution(input: list, parts_list: List[Tuple[int, str, List[Tuple[int, int, int]]]]):
    parts_sum = 0

    for i, line, parts in parts_list:
        for j, char in enumerate(line):
            if char != "*":
                continue

            adjacent_parts = []

            for k in [-1, 0, 1]:
                if i + k < 0 or i + k > len(schematic): # Skip over invalid indicies
                    continue
                for start, end, number in parts_list[i + k][2]:
                    if start <= j <= end:
                        adjacent_parts.append(number)
            
            if len(adjacent_parts) == 2:
                parts_sum += adjacent_parts[0] * adjacent_parts[1]
    
    return parts_sum

schematic = read_input(r'2023/day-3/d3p1-input.txt')
ic(solution(schematic, get_parts(schematic)))
