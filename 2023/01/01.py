import os 
import re


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/input.txt') as f:
        return f.read().split('\n')


def part1(data):
    total = 0
    pattern = re.compile(r'(\d)')
    for line in data:
        matches = pattern.findall(line)
        if len(matches) == 0:
            continue
        first = matches[0]
        if len(matches) == 1:
            total += int(f'{first}{first}')
        else:
            last = matches[-1]
            total += int(f'{first}{last}')
    return total
        
        
def part2(data):
    digit_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4, 
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8, 
        'nine': 9
    }
    total = 0
    digits_pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
    pattern = re.compile(digits_pattern)
    for line in data:
        matches = [int(x) if x.isdigit() else digit_map[x] for x in pattern.findall(line)]
        if len(matches) == 0:
            raise Exception('No matches found')
        first = matches[0]
        last = matches[-1]
        total += first * 10 + last
    return total


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()