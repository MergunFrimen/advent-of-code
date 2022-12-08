from itertools import permutations


def get_data():
    with open('input.txt') as f:
        return [[int(x) for x in line] for line in f.read().split()]


def get_visible(data):
    visible = [[0] * len(data) for _ in range(len(data))]
    size = len(data) - 1
    
    for x in range(len(data)):
        up, down, left, right = [-1 for _ in range(4)]
        for y in range(len(data)):
            if data[x][y] > right:
                right = data[x][y]
                visible[x][y] = 1
            if data[y][x] > down:
                down = data[y][x]
                visible[y][x] = 1
            if data[size - x][size - y] > left:
                left = data[size - x][size - y]
                visible[size - x][size - y] = 1
            if data[size - y][size - x] > up:
                up = data[size - y][size - x]
                visible[size - y][size - x] = 1

    return visible


def part1(data):
    visible = get_visible(data)
    return sum(sum(row) for row in visible)


def get_score(data, i, j):
    total = 1
    size = len(data) - 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        current = 0
        x, y = i + dx, j + dy
        while 0 <= x <= size and 0 <= y <= size and data[i][j] > data[x][y]:
            current += 1
            x, y = x + dx, y + dy
        if 0 <= x <= size and 0 <= y <= size and data[i][j] <= data[x][y]:
            current += 1
        total *= current
    return total


def part2(data):
    score = [[0] * len(data) for _ in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data)):
            score[i][j] = get_score(data, i, j)
    
    return max(max(row) for row in score)


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()