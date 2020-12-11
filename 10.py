#!/usr/bin/env python3

# --- Day 10: Adapter Array --- #

from typing import List


def read(filename: str) -> List[int]:

    with open(filename, 'r') as f:
        data = [int(x) for x in f]

    # Charging outlet
    data = [0] + sorted(data)
    # Built-in device adapter
    data.append(data[-1] + 3)

    return data


def solve_part_one(data: List[int]) -> int:

    c = [y - x for x, y in zip(data, data[1:])]
    return c.count(1) * c.count(3)


def solve_part_two(data):

    memo = dict()

    # Remove the last value (last leaf of each possible branching)
    memo[data.pop()] = 1

    # Go through values of tree backwards 
    # At each node increment its children (even the ones that don't exist)
    for x in reversed(data):
        memo[x] = memo.get(x+1, 0) + memo.get(x+2, 0) + memo.get(x+3, 0)

    # Returns root
    return memo[0]


def main() -> None:

    data = read('input.txt')

    solution1 = solve_part_one(data)
    solution2 = solve_part_two(data)

    print("--- Part One ---")
    print(solution1)
    print("--- Part Two ---")
    print(solution2)


main()
