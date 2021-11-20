from functools import reduce
import operator


def two_mins(l):
    l1 = min(l)
    l.remove(l1)
    l2 = min(l)
    return l1, l2


def ribbon(l):
    x, y = two_mins(l[::])
    return 2*x + 2*y + reduce(operator.mul, l)


# PART 1
def part1():
    with open("input.txt", "r") as f:
        for l, w, h in [map(int, i.split('x')) for i in f.read().split('\n')[:-1]]:
            yield 2*l*w + 2*w*h + 2*h*l + operator.mul(*two_mins([l, w, h]))


# PART 2
def part2():
    with open("input.txt", "r") as f:
        for l, w, h in [map(int, i.split('x')) for i in f.read().split('\n')[:-1]]:
            yield ribbon([l, w, h])


# MAIN
print(sum(part1()))
print(sum(part2()))
