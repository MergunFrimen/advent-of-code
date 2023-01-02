from collections import defaultdict


EMPTY = '.'
FULL = '#'

N = 0
S = 1
E = 2
W = 3


def get_data():
    with open('input.txt') as f:
        return [list(row) for row in f.read().split('\n')[:-1]]


def print_grid(grid):
    (x1, y1), (x2, y2) = min(grid), max(grid)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            print('#' if (i, j) in grid else '.', end='')
        print()
    print()


def part1(data):
    grid = init_grid(data)
    for _ in range(10):
        grid = simulate(grid)
    # print_grid(grid)
    return count_empty(grid)


def init_grid(data):
    grid = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == FULL:
                grid[(i, j)] = {(i, j)}
    return grid


def get_next_move(grid, position):
    i, j = position
    if not get_adjacent(grid, position, N):
        return (i - 1, j)
    if not get_adjacent(grid, position, S):
        return (i + 1, j)
    if not get_adjacent(grid, position, W):
        return (i, j - 1)
    if not get_adjacent(grid, position, E):
        return (i, j + 1)  
    return position


def get_adjacent(grid, position, direction):
    i, j = position
    if direction == N:
        positions = {(i - 1, j + x) for x in range(-1, 2)}
    if direction == S:
        positions = {(i + 1, j + x) for x in range(-1, 2)}
    if direction == E:
        positions = {(i + x, j + 1) for x in range(-1, 2)}
    if direction == W:
        positions = {(i + x, j - 1) for x in range(-1, 2)}
    return positions & set(grid.keys())


def simulate(grid):
    new_grid = defaultdict(set)
    for (i, j) in grid:
        x, y = get_next_move(grid, (i, j))
        new_grid[(x, y)] |= {(i, j)}
    print_grid(new_grid)
    
    final_grid = {}
    for (i, j) in new_grid:
        if len(new_grid[(i, j)]) == 1:
            final_grid[(i, j)] = {(i, j)}
        else:
            for (x, y) in new_grid[(i, j)]:
                final_grid[(x, y)] = (x, y)

    return final_grid


def count_empty(grid):
    (x1, y1), (x2, y2) = min(grid), max(grid)
    area = (x2 - x1) * (y2 - y1)
    return area - len(grid)


def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()