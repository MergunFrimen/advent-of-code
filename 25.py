#!/usr/bin/env python3


from typing import List


def read(filename: str) -> List[int]:
    with open(filename, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]


def solve_part1(data: List[int]) -> int:

    pub_key1, pub_key2 = data

    loop_size1 = get_loop_size(pub_key1)
    loop_size2 = get_loop_size(pub_key2)

    encrypt_key1 = transform(pub_key1, loop_size2)
    encrypt_key2 = transform(pub_key2, loop_size1)
    assert encrypt_key1 == encrypt_key2

    return encrypt_key1 


def get_loop_size(pub_key: int) -> int:

    i = 0
    value = 1
    sub_num = 7

    while True:
        value = (value * sub_num) % 20201227 
        i += 1

        if value == pub_key:
            return i


def transform(sub_num: int, loop_size: int) -> int:

    value = 1

    for _ in range(loop_size):
        value = (value * sub_num) % 20201227 

    return value


def solve_part2(data: List[int]) -> int:
    pass


def main() -> None:
    data = read("input.txt")
    solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    print(f"--- Part One ---\n{solution1}")
    print(f"--- Part Two ---\n{solution2}")


main()
