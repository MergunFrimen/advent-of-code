import os
import re


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/input.txt') as f:
        data = f.read().split('\n')
        result = []
        for row in data:
            digit = 0
            is_digit = False
            lst = []
            for x in row:
                if x.isdigit():
                    is_digit = True
                    digit = digit * 10 + int(x)
                else:
                    if is_digit:
                        lst.append(digit)
                    lst.append(x)
                    is_digit = False
                    digit = 0
            result.append(lst)
        return result


def get_digit_count(number):
    return len(str(number))


def in_bounds(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])


def surrounded_by_symbols(data, i, j, offset):
    j = j + offset
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            x = i + dx
            y = j + dy + offset
            if not in_bounds(data, x, y):
                continue
            element = data[x][y]
            print(x, y, element, i, j, data[i][j - offset])
            if type(element) != int and element != '.':
                return True
    return False


def part1(data):
    total = 0

    for i, row in enumerate(data):
        for j, x in enumerate(row):
            if type(x) == int:
                for offset in range(get_digit_count(x)):
                    if surrounded_by_symbols(data, i, j, offset):
                        total += x
                        break
    
    return total


def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()
