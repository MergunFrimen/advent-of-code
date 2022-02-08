import re
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

dim = {
       3 : 1,
       4 : 3,
       5 : 6,
       6 : 7,
       7 : 6,
       8 : 3,
       9 : 1
       }

def move(position, s):
    position += s
    if position > 10:
        return position - 10
    return position

def count(player_score, position, l, steps, possibility_amount, total):
    if total >= 21:
        player_score[steps] += possibility_amount
        return
    for s, o in dim.items():
        new_position = move(position, s)
        count(player_score, new_position, l, steps + 1, possibility_amount * o, total + new_position)

def compare(p1, p2):
    wins = [0, 0]
    for k1, v1 in p1.items():
        for k2, v2 in p2.items():
            if k1 <= k2:
                wins[0] += v1 * v2
            if k1 > k2:
                wins[1] += v1 * v2
    print(wins)

def part2():
    s1, s2 = read()
    p1, p2 = defaultdict(int), defaultdict(int)
    count(p1, s1, [], 0, 1, 0)
    count(p2, s2, [], 0, 1, 0)
    compare(p1, p2)

part1()
part2()
