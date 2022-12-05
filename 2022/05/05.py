import re


def get_data():
    with open('input.txt') as f:
        stacks, rules = f.read().split('\n\n')
    
    stacks = [re.findall('\w| {4}', stack) for stack in stacks.split('\n')]
    rules = [int(x) for x in rules.split()[1::2]]
    
    new_stacks = [[] for _ in range(int(stacks[-1][-1]))]
    for stack in stacks[-2::-1]:
        for i, cargo in enumerate(stack):
            if cargo.strip() != '':
                new_stacks[i].append(cargo)
    
    new_rules = [[] for _ in range(len(rules) // 3)]
    for i in range(0, len(rules), 3):
        new_rules[i // 3] = rules[i:i+3]

    return new_stacks, new_rules


def part1(data):
    stacks, rules = data
    for amount, from_, to in rules:
        to_move = stacks[from_ - 1][-1:-amount-1:-1]
        stacks[from_ - 1] = stacks[from_ - 1][:-amount]
        stacks[to - 1] += to_move
    return ''.join([stack[-1] for stack in stacks])


def part2(data):
    stacks, rules = data
    for amount, from_, to in rules:
        ## same - only changed list splits
        to_move = stacks[from_ - 1][-amount:]
        stacks[from_ - 1] = stacks[from_ - 1][:-amount]
        stacks[to - 1] += to_move
    return ''.join([stack[-1] for stack in stacks])


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()