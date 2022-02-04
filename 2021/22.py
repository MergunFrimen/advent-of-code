import re

def read():
    with open("input/22.txt") as f:
        return re.findall(r"(\S+) x=([0-9-]+)..([0-9-]+),y=([0-9-]+)..([0-9-]+),z=([0-9-]+)..([0-9-]+)\s*", f.read())

def part1():
    m = read()
    cubes = {}
    for l in m:
        onoff, x1, x2, y1, y2, z1, z2 = (l[0], *map(int, l[1:]))
        if not all(-50 <= i <= 50 for i in map(int, l[1:])):
            continue
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    if onoff == 'on':
                        cubes[(x, y, z)] = 'on'
                    else:
                        cubes[(x, y, z)] = 'off'
    print(list(cubes.values()).count('on'))

def part2():
    m = read()

part1()
part2()
