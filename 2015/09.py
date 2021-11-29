from collections import defaultdict


def bfs(g, r):
    q, e, p = [r], {r}, []
    while q:
        u = q.pop(0)
        for v, d in g[u]:
            if v not in e:
                e.add(v)
                q.append(v)


# PART 1
def part1():
    g = defaultdict(lambda : [])
    with open("input.txt", "r") as f:
        for x in [x.split() for x in f.read().split('\n')[:-1]]:
            g[x[0]].append((x[4], x[2]))


def part2():
    pass


print(part1())
print(part2())
