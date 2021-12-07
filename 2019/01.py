from math import floor

def read():
    with open("input/01.txt") as f:
        return [int(x) for x in f.read().split()]

def part1():
    print(sum(floor(x/3)-2 for x in read()))

def part2():
    s = 0
    for x in read():
        while floor(x/3) - 2 > 0:
            s += floor(x/3) - 2
            x = floor(x/3) - 2
    print(s)

part1()
part2()
