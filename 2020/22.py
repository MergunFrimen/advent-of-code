#!/usr/bin/env python3

from typing import List, Tuple


def read(filename: str) -> Tuple[List[int], List[int]]:

    # Fetch file and split into into player starting decks

    with open(filename, 'r') as f:
        data = f.read()[:-1].split('\n\n')

    p1 = [int(x) for x in data[0].split()[2:]]
    p2 = [int(x) for x in data[1].split()[2:]]

    return (p1, p2)


def solve_part1(p1: List[int], p2: List[int]) -> int:

    while p1 and p2:
        c1, c2 = p1[0], p2[0]

        if c1 > c2:
            p1 = p1[1:] + [c1] + [c2]
            p2 = p2[1:]
        else:
            p1 = p1[1:]
            p2 = p2[1:] + [c2] + [c1]

    winner = p1 if p1 else p2
    return sum([(i + 1) * num for i, num in enumerate(reversed(winner))])


def solve_part2(p1: List[int], p2: List[int],
                h1: List[List[int]], h2: List[List[int]],
                level: int = 0) -> int:

    while p1 and p2:
        # Matching some previous deck in current game
        # Automatic win of player 1
        if p1 in h1 or p2 in h2:
            return 1

        # Add the deck combinations
        h1.append(p1)
        h2.append(p2)

        # Top cards
        c1, c2 = p1[0], p2[0]
        winner = 1 if c1 > c2 else 2

        # Recursive combat sub-game
        if c1 <= len(p1[1:]) and c2 <= len(p2[1:]):
            winner = solve_part2(p1[1:c1 + 1], p2[1:c2 + 1], [], [], level + 1)

        # Player one wins
        if winner == 1:
            p1 = p1[1:] + [c1] + [c2]
            p2 = p2[1:]
        # Player two wins
        if winner == 2:
            p1 = p1[1:]
            p2 = p2[1:] + [c2] + [c1]

    # Return from recursion
    if level != 0:
        return 1 if p1 else 2

    # Calculate cards of winner
    deck = p1 if p1 else p2
    return sum([(i + 1) * num for i, num in enumerate(reversed(deck))])


def main() -> None:
    p1, p2 = read('input.txt')
    solution1 = solve_part1(p1, p2)
    solution2 = solve_part2(p1, p2, [], [], 0)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
