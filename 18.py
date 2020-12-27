#!/usr/bin/env python3


# --- Day 18: Operation Order ---


def read(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read()[:-1].replace(' ', '')
    return data


def solve_part1(data: str) -> int:
    print(data)


def solve_part2(data: str) -> int:
    pass


def main() -> None:
    data = read("input.txt")
    solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    print(f"--- Part One ---\n{solution1}")
    print(f"--- Part Two ---\n{solution2}")


main()
