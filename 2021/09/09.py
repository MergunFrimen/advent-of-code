from operator import mul
from functools import reduce

def read():
    with open("input/09.txt") as f:
        return [[int(x) for x in row] for row in f.read().rstrip().split('\n')]

def check_adjacent(m, i, j):
    for x, y in [(i+x, j+y) for x, y in [(1,0), (-1,0), (0,1), (0,-1)]]:
        if len(m) > x >= 0 and len(m[0]) > y >= 0 and m[i][j] >= m[x][y]:
            return 0
    return m[i][j] + 1

def print_basin(m, visited):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (i, j) in visited:
                print(' ', end='')
            else:
                print(f'{m[i][j]}', end='')
        print()
    print()

def basin_size(m, low):
    visited = [low]
    queue = [low]
    while queue:
        i, j = queue.pop(0) 
        for x, y in [(i+x, j+y) for x, y in [(1,0), (-1,0), (0,1), (0,-1)]]:
            if (x, y) not in visited and len(m) > x >= 0 and len(m[0]) > y >= 0 and m[x][y] != 9 and m[x][y] > m[i][j]:
                visited.append((x, y))
                queue.append((x, y))

    return len(visited)

def part():
    s = 0
    m = read()
    low_points = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            x = check_adjacent(m, i, j)
            s += x
            if m[i][j] == 0 or x != 0:
                low_points.append((i, j))
    print(s)
    print(reduce(mul, sorted([basin_size(m, low) for low in low_points], reverse=True)[:3], 1))

part()
