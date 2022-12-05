import re
from collections import defaultdict
import functools
import itertools
from collections import defaultdict

def read():
    with open("input/21.txt") as f:
        return map(int, re.findall("Player \d starting position: (\d)\s", f.read()))

def part1():
    p1, p2 = read()
    players, scores = [p1 - 1, p2 - 1], [0, 0]
    i = 0
    while max(scores) < 1000:
        players[i % 2] += sum(range(3*i + 1, 3*i + 4))
        scores[i % 2] += players[i % 2] % 10 + 1
        i += 1
    print(3 * i * min(scores))

def move(position, s):
    position += s
    if position > 10:
        return position - 10
    return position

distribution = { 3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1 }

def count(i, w, t1, t2, p1, p2, o1, o2):
    if t1 >= 10:
        w[i] += o1
        return
    for k, v in distribution.items():
        np = move(p1, k)
        count((i + 1) % 2, w, t2, t1 + np, p2, np, o2, o1 * v)

@functools.lru_cache(maxsize=None)
def count(p1, p2, s1, s2):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    w1, w2 = 0, 0
    for x in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        p1_copy = move(p1, sum(x))
        w2_copy, w1_copy = count(p2, p1_copy, s2, s1 + p1_copy)
        w1 += w1_copy
        w2 += w2_copy
    return w1, w2

def part2():
    p1, p2 = read()
    print(max(count(p1, p2, 0, 0)))

part1()
part2()
