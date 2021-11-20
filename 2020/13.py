#!/usr/bin/env python3

from functools import reduce
from typing import List, Tuple

# --- Day 13: Shuttle Search ---


def crt(n: int, a: int) -> int:
    prod = reduce(lambda a, b: a * b, n)
    summary = 0
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        summary += a_i * mul_inv(p, n_i) * p
    return summary % prod


def mul_inv(a: int, b: int) -> int:
    b0 = b
    x0, x1 = 0, 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0
    return x1


def read(filename: str) -> List[Tuple[int, int]]:
    with open(filename, 'r') as f:
        data = f.read()

    time = int(data.split()[0])
    buses = []
    r = 0

    for n in [n for n in data.split()[1].split(',')]:
        if n != 'x':
            buses.append((int(n), int(n) - r))
        r += 1

    return (time, buses)


def solve_part1(data):
    time = data[0]
    buses = [x[0] for x in data[1]]
    start = time

    while True:
        for bus in buses:
            if time % bus == 0:
                return bus * (time - start)
        time += 1


def solve_part2(data):
    return crt([x[0] for x in data], [x[1] for x in data])


def main() -> None:
    data = read('input.txt')
    solution1 = solve_part1(data)
    solution2 = solve_part2(data[1])
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
