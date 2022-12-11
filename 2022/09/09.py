from math import ceil, floor


def get_data():
    with open('input.txt') as f:
        data = [tuple(x.split()) for x in f.read().split('\n')[:-1]]
    DIR = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    return [(DIR[direction], int(steps)) for direction, steps in data]


def addition(pos1, pos2):
    return pos1[0] + pos2[0], pos1[1] + pos2[1]


def subtraction(pos1, pos2):
    return addition(pos1, (-pos2[0], -pos2[1]))


def get_offset(diff):
    x, y = diff
    x = ceil(x / 2) if x > 0 else floor(x / 2)
    y = ceil(y / 2) if y > 0 else floor(y / 2)
    return x, y
    

def simulation(data, knot_amount):
    knots = [(0, 0) for _ in range(knot_amount)]
    visited = set()
    
    for direction, steps in data:
        for _ in range(steps):
            knots[0] = addition(knots[0], direction)
            for i in range(1, len(knots)):
                head, tail = knots[i - 1], knots[i]
                diff = subtraction(head, tail)
                if max(map(abs, diff)) >= 2:
                    offset = get_offset(diff)
                    knots[i] = addition(tail, offset)
            visited.add(knots[-1])
    
    return len(visited)


def part1(data):
    return simulation(data, 2)


def part2(data):
    return simulation(data, 10)


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()