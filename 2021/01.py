def read():
    with open("input.txt") as f:
        return [int(x) for x in f.read().split('\n')[:-1]]


def part1(m):
    s = 0
    for i in range(0, len(m) - 1):
        if m[i] < m[i+1]:
            s += 1
    return s


def part2(m):
    s = 0
    for i in range(0, len(m) - 3):
        if sum(m[i:i+3]) < sum(m[i+1:i+4]):
            s += 1
    return s


print(part1(read()))
print(part2(read()))
