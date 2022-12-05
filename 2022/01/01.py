

def get_data():
    with open('input.txt') as f:
        return [[int(y) for y in x.split()] for x in f.read().split('\n\n')]


def part1(data):
    return max(map(sum, data))


def part2(data):
    return sum(sorted(map(sum, data))[-3:])


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()