def read():
    with open("input.txt") as f:
        return [int(x) for x in f.read().split()]


def part1(m, s, start):
    total = 0

    if s == 0:
        return 1

    for i in range(start, len(m)):
        if s - m[i] >= 0:
            total += part1(m, s - m[i], i + 1)

    return total


def part2(m, s, start):
    l = []
    part2_rec(m, s, start, 0, l)
    return l.count(min(l))


def part2_rec(m, s, start, d, l):
    if s == 0:
        l.append(d)
        return 1

    for i in range(start, len(m)):
        if s - m[i] >= 0:
            part2_rec(m, s - m[i], i + 1, d + 1, l)


print(part1(read(), 150, 0))
print(part2(read(), 150, 0))
