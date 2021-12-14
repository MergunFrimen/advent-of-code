import re
from collections import Counter

def read():
    with open("input/14.txt") as f:
        m = f.read().split("\n\n")
    return m[0], {k:v for k,v in re.findall("(\S+) -> (\S+)", m[1])}

def part(max_depth):
    template, rules = read()
    template = [template[i:i+2] for i in range(len(template) - 1)]
    count = {k:0 for k in set(rules.values())}

    i = -1
    for x in template:
        i = rec(rules, x, max_depth, 0, i + 1, count)
        print(i)

    print(count)

def rec(rules, x, max_depth, depth, i, count):
    if depth == max_depth:
        count[x[0]] += 1
        if i == 3 * sum(2**i for i in range(max_depth + 1)) - 1:
            count[x[1]] += 1
        return i
    
    new = rules[x]
    left, right = x[0] + new, new + x[1]

    i = rec(rules, left, max_depth, depth + 1, i + 1, count)
    return rec(rules, right, max_depth, depth + 1, i + 1, count)

part(2)
