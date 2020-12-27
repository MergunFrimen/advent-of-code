#!/usr/bin/env python3

from typing import List

Cube = List[List[List[int]]]

def read(filename: str) -> Cube:
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]

    result = []
    size = len(data)
    inactive = [[0 for _ in range(size)] for _ in range(size)]

    # Add active row
    for row in data:
        temp = []
        for x in row:
            if x == '#':
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)

    print(result)


def solve_part1(cube: Cube) -> int:
    pass


def solve_part2(cube: Cube) -> int:
    pass


def main() -> None:
    cube = read("input.txt")
    solution1 = solve_part1(cube)
    solution2 = solve_part2(cube)
    print(f"--- Part One ---\n{solution1}")
    print(f"--- Part Two ---\n{solution2}")


main()
