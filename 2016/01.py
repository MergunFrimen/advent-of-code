def read():
    with open("input.txt") as f:
        return f.read().split(', ')

def part1():
    dirs_change = ['N', 'E', 'S', 'W']
    dirs = {'N':(0, 1), 'E':(1, 0), 'S':(0, -1), 'W':(-1, 0)}
    p = [0, 0]
    d = "N"
    for m in read():
        if m[0] == 'L':
            d = dirs_change[(dirs_change.index(d)-1) % 4]
        if m[0] == 'R':
            d = dirs_change[(dirs_change.index(d)+1) % 4]
        p[0] += dirs[d][0] * int(m[1:])
        p[1] += dirs[d][1] * int(m[1:])
    print(sum(map(abs, p)))

def part2():
    dirs_change = ['N', 'E', 'S', 'W']
    dirs = {'N':(0, 1), 'E':(1, 0), 'S':(0, -1), 'W':(-1, 0)}
    p = [0, 0]
    d = "N"
    visited = set(tuple(p))
    for m in read():
        if m[0] == 'L':
            d = dirs_change[(dirs_change.index(d)-1) % 4]
        if m[0] == 'R':
            d = dirs_change[(dirs_change.index(d)+1) % 4]
        for _ in range(int(m[1:])):
            p[0] += dirs[d][0]
            p[1] += dirs[d][1]
            if tuple(p) in visited:
                print(sum(map(abs, p)))
                return
            visited.add(tuple(p))

part1()
part2()
