import os 


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/input.txt') as f:
        pass


def part1(data):
    pass


def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()