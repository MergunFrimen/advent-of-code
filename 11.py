#!/usr/bin/env python3

# --- Day 11: Seating System ---

from typing import List
from copy import deepcopy


def read(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        seating = [[x for x in y[:-1]] for y in f]
    # Pad with empty
    # for x in range(abs(len(seating) - len(seating)[0])):
    #     seating.append([])
    return seating


def solve_part1(seating: List[List[str]]) -> int:
 
    seating = deepcopy(seating)

    # Reaches equilibrium and returns number of occupied seats
    while True:
        seating, previous = iterate1(seating), seating
        if previous == seating:
            return occupied_seats_count(seating)


def occupied_seats_count(seating):
    return sum([1 for i in range(len(seating)) for j in range(len(seating[0])) if seating[i][j] == '#'])


def print_seating(seating):

    for i in range(len(seating)):
        for j in range(len(seating[0])):
            print(seating[i][j], end='')
        print()
    print()


def iterate1(seating: List[List[str]]):

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
    return 0 <= seat[0] < len(seating) and 0 <= seat[1] < len(seating[0])


def iterate2(seating: List[List[str]]):

    new_seating = deepcopy(seating)

    for i in range(len(seating)):
        for j in range(len(seating[0])):

            if seating[i][j] == 'L' and adjacent_occupied_count2(seating, i, j) == 0:
                new_seating[i][j] = '#'
            elif seating[i][j] == '#' and adjacent_occupied_count2(seating, i, j) >= 5:
                new_seating[i][j] = 'L'

    return new_seating


def adjacent_occupied_count2(seating, row, col):

    left = (0, -1)
    right = (0, 1)
    up = (-1, 0)
    down = (1, 0)

    start = (row, col)
    counter = 0

    counter += check_direction(seating, start, up)
    counter += check_direction(seating, start, down)
    counter += check_direction(seating, start, left)
    counter += check_direction(seating, start, right)
    counter += check_direction(seating, start, myadd(up, right))
    counter += check_direction(seating, start, myadd(up, left))
    counter += check_direction(seating, start, myadd(down, right))
    counter += check_direction(seating, start, myadd(down, left))

    return counter


def check_direction(seating, start, direction):

    while True:

        start = myadd(start, direction)

        if not bounded(seating, start):
            return 0
        if seating[start[0]][start[1]] == 'L':
            return 0
        if seating[start[0]][start[1]] == '#':
            return 1
   

def myadd(xs,ys):
     return tuple(x + y for x, y in zip(xs, ys))


def solve_part2(seating: List[List[str]]) -> int:
    
    seating = deepcopy(seating)
   
    while True:
        seating, previous = iterate2(seating), seating
        if previous == seating:
            return occupied_seats_count(seating)


def main() -> None:

    seating = read('input.txt')
    #solution1 = solve_part1(seating)
    solution2 = solve_part2(seating)
    #print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
