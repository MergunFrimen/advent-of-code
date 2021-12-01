from copy import deepcopy
from os import system


def read():
    with open("input.txt") as f:
        return [[(1 if y == '#' else 0) for y in x] for x in f.read().split('\n')[:-1]]


def neighboor_sum(m, x, y):
    n = 0
    for i in [x + x2 for x2 in [-1, 0, 1]]:
        for j in [y + y2 for y2 in [-1, 0, 1]]:
            if (i, j) != (x, y) and i not in [-1, len(m)] and j not in [-1, len(m)]:
                n += m[i][j]
    return n


def part1(m, steps=100):
    for _ in range(steps):
        p = deepcopy(m)
        for i in range(len(m)):
            for j in range(len(m)):
                if p[i][j] == 1 and neighboor_sum(p, i, j) not in [2, 3]:
                    m[i][j] = 0
                if p[i][j] == 0 and neighboor_sum(p, i, j) == 3:
                    m[i][j] = 1
        
        system("clear")
        for i in range(len(m)):
            print(''.join(map(lambda x : '# ' if x == 1 else '. ', m[i])))
        print()

    return sum(map(sum, m))


def part2(m, steps=100):
    for _ in range(steps):
        for i, j in [(0,0),(0,len(m)-1),(len(m)-1,0),(len(m)-1,len(m)-1)]:
            m[i][j] = 1
        p = deepcopy(m)
        for i in range(len(m)):
            for j in range(len(m)):
                if (i,j) in [(0,0),(0,len(m)-1),(len(m)-1,0),(len(m)-1,len(m)-1)]:
                    continue
                if p[i][j] == 1 and neighboor_sum(p, i, j) not in [2, 3]:
                    m[i][j] = 0
                if p[i][j] == 0 and neighboor_sum(p, i, j) == 3:
                    m[i][j] = 1
        
        system("clear")
        for i in range(len(m)):
            print(''.join(map(lambda x : '# ' if x == 1 else '. ', m[i])))
        print()

    return sum(map(sum, m))


# print(part1(read()))
print(part2(read()))
