def read():
    with open("input/02.txt") as f:
        return [x.split() for x in f.read().split('\n')[:-1]]


def part1(m):
    r = [0, 0]
    for x, y in m:
        if x == 'forward':
            r[0] += int(y)
        elif x == 'up':
            r[1] -= int(y)
        elif x == 'down':
            r[1] += int(y)
    return r[0] * r[1]


def part2(m):
    r = [0, 0, 0]
    for x, y in m:
        if x == 'forward':
            r[0] += int(y)
            r[1] += r[2] * int(y)
        elif x == 'up':
            r[2] -= int(y)
        elif x == 'down':
            r[2] += int(y)
    return r[0] * r[1]


print(part1(read()))
print(part2(read()))
