def read():
    with open("input/03.txt") as f:
        return f.read().split()


def part1(m):
    x = [0 for _ in range(len(m[0]))]
    for w in m:
        for i in range(len(w)):
            if w[i] == '1':
                x[i] += 1
            else:
                x[i] -= 1
    g = int(''.join(map(lambda i : '1' if i > 0 else '0', x)), 2)
    e = int(''.join(map(lambda i : '1' if i < 0 else '0', x)), 2)
    return g * e


def part2(m):
    m = [[int(b) for b in w] for w in m]
    o = [0 for _ in range(len(m[0]))]
    s = [0 for _ in range(len(m[0]))]

    for i in range(len(m[0])):
        wo = list(filter(lambda a : a[:i] == o[:i], m))
        if len(wo) == 1:
            o = wo[0]
            break
        for w in wo:
            if w[i] == 1:
                o[i] += 1
            else:
                o[i] -= 1
        o[i] = 1 if o[i] >= 0 else 0

    for i in range(len(m[0])):
        so = list(filter(lambda a : a[:i] == s[:i], m))
        if len(so) == 1:
            s = so[0]
            break
        for w in so:
            if w[i] == 1:
                s[i] += 1
            else:
                s[i] -= 1
        s[i] = 0 if s[i] >= 0 else 1

    return int(''.join(map(str, o)), 2) * int(''.join(map(str, s)), 2)


print(part1(read()))
print(part2(read()))
