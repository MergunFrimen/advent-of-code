

def get_data():
    with open('input.txt') as f:
        return f.read().split()[0]


def markers(data, amount):
    for i in range(len(data)):
        if len(set(data[i:i+amount])) == amount:
            return i + amount


def part1(data):
    return markers(data, 4)


def part2(data):
    return markers(data, 14)


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()