#!/usr/bin/env python3

from itertools import permutations


# --- Day 16: Ticket Translation ---

def read(filename: str):
    with open(filename, 'r') as f:
        raw = f.read()[:-1]

    result = []
    data, my, other = raw.split('\n\n')
    my = my.split('\n')[1].split(',')
    other = [x.split(',') for x in other.split('\n')[1:]]

    for row in data.split('\n'):
        type, intervals = row.split(': ', 1)
        result.append((type, intervals.split(' or ')))

    return (result, my, other)


def solve_part1(data):
    
    types, my, other = data
    error_rate = 0

    for ticket in other:
        for x in ticket:
            x = int(x)
            if not validate_range(types, x):
                error_rate += x
                break

    return error_rate


def solve_part2(data):
    
    types, my, other = data
    other += [my]
    
    # Filter out invalid tickets
    for ticket in other[:]:
        for x in ticket:
            x = int(x)
            if not validate_range(types, x):
                other.remove(ticket)
                break

    options = list()

    # Get mapping 
    for name, ranges in types:
        for col in range(len(other[0])):
            if check_columns(ranges, other, col):
                options.append((name, col))

    result = dict()
    options = list(sorted(options, key=lambda x: x[0]))
    groups = group(options)
    process = groups.copy()
    i = 0

    # for k, v in groups.items():
    #     print(k, v)

    # Filter out
    while process:
        key = list(process.keys())[i % len(process)]
        if len(process[key]) == 1:
            val = process[key][0]
            process = remove_items(process, val) 
            result[key] = val
            del process[key]
        i += 1

    result = dict(sorted(result.items(), key=lambda item: item[1])) 
    multiply = 1

    for k, v in result.items():
        if k.split()[0] == "departure":
            multiply *= int(my[v])

    return multiply


def remove_items(process, key):
    for k in process:
        if key in process[k]:
            process[k].remove(key)
    return process


def group(options):
    i = 0
    groups = dict()
    while i < len(options):
        name, value = options[i]
        if name in groups:
            groups[name].append(value)
        else:
            groups[name] = [value]
        i += 1
    return groups
                

def check_columns(ranges, other, col):
    r1, r2 = ranges
    i1, j1 = r1.split('-')
    i2, j2 = r2.split('-')

    for row in other:
        x1 = int(row[col]) in range(int(i1), int(j1) + 1)
        x2 = int(row[col]) in range(int(i2), int(j2) + 1)
        if not x1 and not x2:
            return False
    return True

 
def validate_range(types, x):
    for _, ranges in types: 
        r1, r2 = ranges
        i1, j1 = r1.split('-')
        i2, j2 = r2.split('-')
        if x in range(int(i1), int(j1) + 1) or x in range(int(i2), int(j2) + 1):
            return True
    return False


def main() -> None:
    data = read('input.txt')
    solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
