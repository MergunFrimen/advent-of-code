with open("input/02.txt") as f:
    m = [[int(y) for y in x.split()] for x in f.read().rstrip().split('\n')]
print(sum(max(x) - min(x) for x in m))
print(sum(max(r[i], r[j])//min(r[i], r[j]) for r in m for i in range(len(r)) for j in range(i, len(r)) if i != j and max(r[i], r[j]) % min(r[i], r[j]) == 0))
