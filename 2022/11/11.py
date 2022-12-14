from re import findall
from collections import deque
from operator import mul
from functools import reduce


def get_data():
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    monkeys = []
    for i, monkey in enumerate([x.split('\n')[1:] for x in data]):
        items = [int(x) for x in findall('\d+', monkey[0])]
        ops = findall('[\*+] old|[\*+] \d+', monkey[1])[0]
        test = [int(x) for x in findall('\d+', ''.join(monkey[2:]))]
        monkeys.append([i, deque(items), ops, test])
    return monkeys


def part1(data):
    counter = [0 for _ in data]
    for i in range(20):
        for monkey in data:
            for item in monkey[1]:
                operand = int(monkey[2][2:]) if 'old' not in monkey[2] else item
                worry = (item * operand) if monkey[2][0] == '*' else (item + operand)
                worry //= 3
                next_monkey = monkey[3][1] if worry % monkey[3][0] == 0 else monkey[3][2]
                data[next_monkey][1].append(worry)
                counter[monkey[0]] += 1
            monkey[1] = []
    counter.sort()
    return counter[-1] * counter[-2]
            

def part2(data):
    counter = [0 for _ in data]
    modulo = reduce(mul, [x[3][0] for x in data])
    for i in range(10000):
        for monkey in data:
            for item in monkey[1]:
                operand = int(monkey[2][2:]) if 'old' not in monkey[2] else item
                worry = (item * operand) if monkey[2][0] == '*' else (item + operand)
                # worry //= 3
                worry %= modulo
                next_monkey = monkey[3][1] if worry % monkey[3][0] == 0 else monkey[3][2]
                data[next_monkey][1].append(worry)
                counter[monkey[0]] += 1
            monkey[1] = []
    counter.sort()
    return counter[-1] * counter[-2]


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()