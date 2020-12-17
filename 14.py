#!/usr/bin/env python3

from copy import deepcopy
import re


# --- Day 14: Docking Data ---


def read(filename: str):
    with open(filename, 'r') as f:
        data = f.read()[:-1]

    memory = []

    for group in data.split('mask = ')[1:]:
        row = [x.lstrip('mem[').rstrip(']') for x in group.split()[1:] if x != '=']
        memory.append((group.split()[0], [x for x in zip(row[::2], row[1::2])]))

    return memory


def solve_part1(data):

    memory = dict()
    
    for mask, actions in data:
        print(mask)

        for x in actions:
            pass



def main() -> None:
    data = read('input.txt')
    solution1 = solve_part1(data)
    print("--- Part One ---\n", solution1)


main()
