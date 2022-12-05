from collections import defaultdict

def rec(g, visited, revisit):
    if visited[-1] == 'end':
        return 1
    s = 0
    for child in g[visited[-1]]:
        if child.isupper() or child not in visited:
            s += rec(g, visited + [child], revisit)
        elif child.islower() and child in visited and child != 'start' and revisit:
            s += rec(g, visited + [child], False)
    return s

g = defaultdict(list)
for f, t in [x.split('-') for x in open("input/12.txt").read().split()]:
    g[f].append(t)
    g[t].append(f)

print(rec(g, ['start'], False))
print(rec(g, ['start'], True))
