#!/usr/bin/env python3

# --- Day 11: Seating System ---

from typing import List
from copy import deepcopy


def read(filename: str) -> List[List[str]]:
    
    with open(filename, 'r') as f:
        seating = [[x for x in y[:-1]] for y in f]
    return seating


def solve_part1(seating: List[List[str]]) -> int:
    
    while True:
        previous = seating
        seating = iterate(seating)

        if previous == seating:
            return sum([1 for i in range(len(seating)) for j in range(len(seating[0])) if seating[i][j] == '#'])


def print_seating(seating):

    for i in range(len(seating)):
        for j in range(len(seating[0])):
            print(seating[i][j], end='')
        print()
    print()


def iterate(seating: List[List[str]]):

    new_seating = deepcopy(seating)

    for i in range(len(seating)):
        for j in range(len(seating[0])):

            if seating[i][j] == 'L' and adjacent_occupied_count(seating, i, j) == 0:
                new_seating[i][j] = '#'
            elif seating[i][j] == '#' and adjacent_occupied_count(seating, i, j) >= 4:
                new_seating[i][j] = 'L'

    return new_seating


def adjacent_occupied_count(seating, row, col):

    adjacent_seats = [(row+i, col+j) for i in [-1, 0, +1] for j in [-1, 0, +1]]
    adjacent_seats = filter(lambda seat: seat != (row, col) and bounded(seating, seat), adjacent_seats)
    return sum([1 for i, j in adjacent_seats if seating[i][j] == '#'])


def bounded(seating, seat) -> bool:

    return (0 <= seat[0] < len(seating) and
            0 <= seat[1] < len(seating[0]))


def solve_part2(seating: List[List[str]]) -> int:
    return None


def main() -> None:

    seating = read('input.txt')
    solution1 = solve_part1(seating)
    solution2 = solve_part2(seating)

    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
