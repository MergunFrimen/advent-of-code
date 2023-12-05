import os 
import re


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/input.txt') as f:
        pattern = r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)"
        data = f.read().split('\n')
        result = []
        for row in data:
            match = re.findall(pattern, row)
            num, left, right = match[0][0], match[0][1], match[0][2]
            left = [int(x) for x in left.split() if x.isdigit()]
            right = [int(x) for x in right.split() if x.isdigit()]
            result.append((num, set(left), right))
        return result


def part1(data):
    total = 0
    for _, left, right in data:
        print(left, right)
        exp = 0
        for x in right:
            if x in left:
                exp += 1
        if exp > 0:
            total += 2**(exp - 1)
            print(exp, total)
    return total


def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()