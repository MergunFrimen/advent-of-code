from collections import defaultdict

def read():
    with open("input.txt") as f:
        return [[y.split(',') for y in x.split(" -> ")] for x in f.read().split('\n')[:-1]]

def part(p):
    lines = read()
    m = defaultdict(int)
    for f, t in lines:
        f = [int(x) for x in f]
        t = [int(x) for x in t]
        if f[0] == t[0]:
            for i in range(min(f[1], t[1]), max(f[1], t[1]) + 1):
                m[(f[0], i)] += 1
        elif f[1] == t[1]:
            for i in range(min(f[0], t[0]), max(f[0], t[0]) + 1):
                m[(i, f[1])] += 1
        elif p == 2:
            x, y = 1 if t[0] - f[0] > 0 else -1, 1 if t[1] - f[1] > 0 else -1
            for i in range(abs(t[0] - f[0]) + 1):
                m[(f[0] + i*x, f[1] + i*y)] += 1 

    print(sum(1 for x in m if m[x] >= 2))

part(1)
part(2)
