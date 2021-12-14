import re
from collections import Counter

def read():
    with open("input/14.txt") as f:
        m = f.read().split("\n\n")
    return m[0], {k:v for k,v in re.findall("(\S+) -> (\S+)", m[1])}

def part1():
    template, rules = read()
    for _ in range(10):
        new = [] 
        for i in range(len(template) - 1):
            k = template[i:i+2]
            new += [template[i], rules[k]]
        template = ''.join(new + [template[-1]])
    c = Counter(template).values()
    print(max(c) - min(c))

def part2():
    pass

part1()
part2()
