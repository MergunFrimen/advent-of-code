#!/usr/bin/env python3

import numpy as np


def read(filename: str):
    with open(filename, 'r') as f:
        raw = f.read()

    # (tile_id, np.matrix)
    data = []

    # Parse title_id and matrix
    for tile in raw.split('\n\n'):
        tile_id = int(tile.split(':')[0].split()[1])
        matrix = tile.split(':')[1].split()

        # Transform into numbers
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == '#':
                    row.append(1)
                else:
                    row.append(0)
            matrix[i] = row
        data.append((tile_id, np.matrix(matrix)))

    return data


def solve_part1(data):
    
    base = data.pop()
    size = base[1].size
    mapping_matrix = np.matrix([[0 for _ in range(size)] for _ in range(size)])
    
    while data:
        pass


def main():
    data = read('input.txt')
    solution1 = solve_part1(data)
    print("--- Part One ---\n", solution1)


main()
