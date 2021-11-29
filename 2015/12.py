def part1():
    s = 0
    with open("input.txt") as f:
        for x in f.read().split(','):
            x = x.translate({ord(i): None for i in '{}[]'}).rstrip()
            if not x:
                continue
            if ':' in x:
                x = x.split(':')[-1]
            if x[0] != '"':
                s += int(x)
    return s


def part2():
    r = False
    s = []
    with open("input.txt") as f:
        for x in f.read().split(','):
            if x[0] in '{[':
                s.append(x[0])
            if x[0] in '}]':
                s.pop()


print(part1())
print(part2())
