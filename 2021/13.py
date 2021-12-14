import re

def read():
    with open("input/13.txt") as f:
        m = f.read().split('\n\n')
    points = list(map(lambda x : (int(x[0]), int(x[1])),re.findall(r"(\d+),(\d+)", m[0])))
    folds = list(map(lambda x : (x[0], int(x[1])),re.findall(r"fold along (.)=(.+)", m[1])))
    return points, folds

def create_grid(points):
    x, y = [x for x, _ in points], [y for _, y in points]
    g = [['.' for _ in range(abs(max(x) + 1))] for _ in range(abs(max(y) + 1))]
    for i, j in points:
        g[j][i] = '#'
    return g

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def fold_y(g, y):
    new = g[:y]
    for i in range(y + 1, len(g)):
        for j in range(len(g[0])):
            if g[i][j] == '#':
                new[y - i][j] = '#'
    return new

def fold_x(g, x):
    new = [row[:x] for row in g]
    for i in range(len(g)):
        for j in range(x + 1, len(g[0])):
            if g[i][j] == '#':
                new[i][x - j] = '#'
    g = new

def part():
    points, folds = read()
    g = create_grid(points)

    for i, f in enumerate(folds):
        if f[0] == 'x':
            fold_x(g, f[1])
        else:
            fold_y(g, f[1])
        if i == 0:
            print(sum(row.count('#') for row in g))
    print_grid(g)

part()
