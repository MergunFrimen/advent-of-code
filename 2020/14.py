#!/usr/bin/env python3

from copy import deepcopy
from itertools import permutations, product
import re


# --- Day 14: Docking Data ---


def read(filename: str):
    with open(filename, 'r') as f:
        data = f.read()[:-1]

    memory = []
    for group in data.split('mask = ')[1:]:
        row = [x.lstrip('mem[').rstrip(']') for x in group.split()[1:] if x != '=']
        mask = group.split()[0] 
        actions = [(int(x), int(y)) for x, y in zip(row[::2], row[1::2])]
        memory.append((mask, actions))

    return memory


def solve(data, part):

    memory = dict()
    for mask, actions in data:
        for addr, num in actions:
            
            # Solve part 1
            if part == 1:
                memory[addr] = process1(mask, num)

            # Solve part 2
            if part == 2:
                for x in process2(memory, mask, addr):
                    memory[x] = num

    return sum([x for x in memory.values()])


def process1(mask, num):
    num = pad(len(mask), "{:0b}".format(num))
    new = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            new += num[i]
        else:
            new += mask[i]
    return int(new, 2) 


def process2(memory, mask, addr):
    addr = pad(len(mask), "{:0b}".format(addr))
    addresses = []
    new = ""
    
    # Bitwise operation on addr
    for i in range(len(mask)):
        if mask[i] == 'X':
            new += 'X'
        else:
            new += str(int(mask[i]) | int(addr[i]))

    # Compute address permutations
    for permutation in [pad(mask.count('X'), "{:0b}".format(x)) for x in range(2**new.count('X'))]:
        copy = new
        for bit in permutation:
            copy = copy.replace('X', bit, 1)
        addresses.append(copy)

    return addresses
 

def pad(amount, num) -> str:
    return '0'*(amount - len(num)) + num


def main() -> None:
    data = read('input.txt')
    solution1 = solve(data, 1)
    solution2 = solve(data, 2)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
