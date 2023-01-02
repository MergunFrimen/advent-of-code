# from _ import _


def get_data():
    with open('input.txt') as f:
        return [tuple(map(int, x.split(','))) for x in f.read().split()]


def part1(data):
    visible = {x:6 for x in data}
    for x in data:
        for n in get_neighbors(x):
            if n in visible:
                visible[n] -= 1
    return sum(visible.values())


def get_neighbors(position):
    position = list(position)
    neighbors = []
    for i in range(-1, 2, 2):
        for j in range(len(position)):
            x, y, z = position[:j], [position[j] + i], position[j+1:]
            neighbors += [tuple(x + y + z)]
    return neighbors



def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()