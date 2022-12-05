

def get_data():
    with open('input.txt') as f:
        data = [x.split(',') for x in f.read().split()]
        data = [[tuple(map(int, y.split('-'))) for y in x] for x in data]
        return data


def part1(data):
    count = 0
    for (x, y), (i, j) in data:
        if i <= x <= y <= j or x <= i <= j <= y:
            count += 1
    return count


def part2(data):
    count = 0
    for (x, y), (i, j) in data:
        if i <= x <= j or i <= y <= j or \
            x <= i <= y or x <= j <= y:
            count += 1
    return count


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()