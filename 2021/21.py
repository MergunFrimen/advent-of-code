import re

dim = {
       3 : 1,
       4 : 3,
       5 : 6,
       6 : 7,
       7 : 6,
       8 : 3,
       9 : 1 
       }

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

def move_player(players, scores, i):
    players[i % 2] += sum(range(3*i + 1, 3*i + 4))
    scores[i % 2] += players[i % 2] % 10 + 1
    return i + 1

def part2():
    p1, p2 = read()
    players, scores, m = (p1 - 1, p2 - 1), (0, 0), [0, 0]
    rec(players, scores, m, 1, 0)
    print(m)

def rec(p, s, m, t, i):
    p1, p2 = p
    s1, s2 = s

    if s1 >= 21:
        m[0] += t
        return
    elif s2 >= 21:
        m[1] += t
        return

    for x in range(3, 10):
        if i % 2 == 0:
            new_p = (p1 + x, p2)
            new_s = (s1 + new_p[0] % 10 + 1, s2)
        else:
            new_p = (p1, p2 + x)
            new_s = (s1, s2 + new_p[1] % 10 + 1)
        rec(new_p, new_s, m, t * dim[x], i + 1)

part1()
part2()
