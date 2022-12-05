import re

def read():
    with open("input/17.txt") as f:
        return re.findall(r"target area: x=(\S\d+)..(\S\d+), y=(\S\d+)..(\S\d+)\s*", f.read())[0]

def part1():
    x1, x2, y1, y2 = map(int, read())

def part2():
    x1, x2, y1, y2 = map(int, read())

part1()
part2()
