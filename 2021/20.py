#!/usr/bin/python

from copy import deepcopy

def read():
    with open("input/20.txt") as f:
        algo, imag = f.read().rstrip().split('\n\n')
    return algo, [[i for i in row] for row in imag.split()]

def index(m, i, j, c):
    l = {'#': '1', '.': '0'}
    area = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if 0 <= i+x < len(m) and 0 <= j+y < len(m):
                area.append(l[m[i+x][j+y]])
            else:
                area.append(l[c])
    return int(''.join(area), 2)

def expand(m, c):
    new_m = [[c for _ in range(len(m) + 2)] for _ in range(len(m) + 2)]
    for i in range(len(m)):
        for j in range(len(m)):
            new_m[i + 1][j + 1] = m[i][j]
    return new_m

def iteration(image, algo, current):
    image = expand(image, current)
    m = deepcopy(image)
    l = {'#': '1', '.': '0'}
    for i in range(len(image)):
        for j in range(len(image)):
            m[i][j] = algo[index(image, i, j, current)]
    return algo[int(''.join(l[current]*9), 2)], m

def count_lit_pixels(m):
    return sum([row.count('#') for row in m])

def print_grid(m):
    for row in m:
        print(''.join(row))
    print()

def part(amount):
    algo, image = read()
    current = '.'
    for _ in range(amount):
        current, image = iteration(image, algo, current)
    print(count_lit_pixels(image))

part(2)
part(50)
