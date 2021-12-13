def read():
    with open("input/12.txt") as f:
        return [x.split('-') for x in f.read().split()]

def create_graph():
    m = read()
    g = {k[0]:[] for k in m}
    for f, t in m:
        g[t] = []
        g[f] = []
    for f, t in m:
        g[t].append(f)
        g[f].append(t)
    return g

def part1():
    g = create_graph()
    visited = []

def part2():
    m = read()

part1()
part2()
