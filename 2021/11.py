def read():
    with open("input/11.txt") as f:
        return [[int(x) for x in row] for row in f.read().split('\n')[:-1]]

def surrounding(m, i, j):
    dv = [(x+i, y+j) for x in [-1, 0, 1] for y in [-1,0,1] if x or y]
    return filter(lambda x : len(m) > x[0] >= 0 and len(m) > x[1] >= 0, dv)

def print_grid(m):
    for row in m:
        print(' '.join(str(x) for x in row))
    print("")

def part(steps):
    m = read()
    s = 0
    while steps != 0: 
        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j] += 1
        flashed = True
        deactivate = []
        while flashed:
            activate = []
            flashed = False
            for i in range(len(m)):
                for j in range(len(m[i])):
                    if m[i][j] > 9:
                        flashed = True
                        deactivate.append((i, j))
                        for x, y in surrounding(m, i, j):
                            activate.append((x, y))
            for i, j in activate:
                m[i][j] += 1
            for i, j in deactivate:
                m[i][j] = 0
        s += sum(row.count(0) for row in m)
        if sum(row.count(0) for row in m) == len(m)**2:
            print_grid(m)
            return steps
        steps -= 1
    print(s)

part(100)
print(part(-1))
