#!/usr/bin/env python3

from typing import List


# --- Day 15: Rambunctious Recitation ---


def solve(data: List[int], count: int) -> int:

    # Iteration nums are indexes in list
    memory = [0] * count

    # Fill in with data values except for last
    for i, x in enumerate(data[:-1]):
        memory[x] = i + 1

    # Start with last num in data
    pos = len(data)
    init = data[-1]

    while pos <= count:
        if memory[init] == 0:
            initnew = 0
        else:
            initnew = pos - memory[init]
        memory[init] = pos
        init = initnew
        pos += 1

    return memory.index(count)
   

def main() -> None:

    data = [15, 5, 1, 4, 7, 0]
    solution1 = solve(data, 2020)
    solution2 = solve(data, 30000000)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
