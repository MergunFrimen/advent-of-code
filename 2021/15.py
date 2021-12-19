import math

def read():
    with open("input/15.txt") as f:
        return [[int(x) for x in row] for row in f.read().split()]

def get_nodes(m, p, visited):
    i, j = p
    nodes = []
    for x, y in [(i+x, j+y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
        if len(m) > x >= 0 and len(m[0]) > y >= 0 and (x, y) not in visited:
            nodes.append((x, y))
    return nodes

def part1():
    m = read()
    distances = {(i, j):math.inf for i in range(len(m)) for j in range(len(m[0]))}
    distances[(0,0)] = 0
    while math.inf in distances.values():
        u = 


def part2():
    m = read()

part1()
part2()
