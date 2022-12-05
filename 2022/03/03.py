

def get_data():
    with open('input.txt') as f:
        return [x for x in f.read().split()]


def part1(data):
    total = 0
    for rucksack in data:
        middle = len(rucksack) // 2
        shared_item = set(rucksack[:middle]) & set(rucksack[middle:])
        total += get_priority(shared_item.pop())
    return total


def get_priority(item):
    if item.isupper():
        return ord(item) - 65 + 27
    return ord(item) - 96


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        group = list(map(set, data[i:i+3]))
        total += get_priority(group[0].intersection(group[1], group[2]).pop())
    return total


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()