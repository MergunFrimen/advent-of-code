from PIL import Image


def turn1(g, p):
    x = list(map(int, p[1].split(',')))
    y = list(map(int, p[3].split(',')))
    for i in range(x[0], y[0] + 1):
        for j in range(x[1], y[1] + 1):
            if p[0] == 'on':
                g[i][j] = 1
            else:
                g[i][j] = 0


def toggle1(g, p):
    x = list(map(int, p[0].split(',')))
    y = list(map(int, p[2].split(',')))
    for i in range(x[0], y[0] + 1):
        for j in range(x[1], y[1] + 1):
            if g[i][j] == 1:
                g[i][j] = 0
            else:
                g[i][j] = 1


def turn2(g, p):
    x = list(map(int, p[1].split(',')))
    y = list(map(int, p[3].split(',')))
    for i in range(x[0], y[0] + 1):
        for j in range(x[1], y[1] + 1):
            if p[0] == 'on':
                g[i][j] += 1
            elif g[i][j] > 0:
                g[i][j] -= 1


def toggle2(g, p):
    x = list(map(int, p[0].split(',')))
    y = list(map(int, p[2].split(',')))
    for i in range(x[0], y[0] + 1):
        for j in range(x[1], y[1] + 1):
            g[i][j] += 2


# PART 1
def part1():
    g = [[0 for _ in range(1000)] for _ in range(1000)]
    with open("input.txt", "r") as f:
        for line in f.read().split('\n')[:-1]:
            t, *p = line.split()
            if t == "turn":
                turn1(g, p)
            if t == "toggle":
                toggle1(g, p)

    img  = Image.new(mode = "RGB", size = (1000, 1000))
    pixels = img.load()
    for i in range(1000):
        for j in range(1000):
            if g[i][j] == 1:
                pixels [i,j] = (255, 255, 255)
    img.show()

    return sum([sum(x) for x in g])


# PART 2
def part2():
    g = [[0 for _ in range(1000)] for _ in range(1000)]
    with open("input.txt", "r") as f:
        for line in f.read().split('\n')[:-1]:
            t, *p = line.split()
            if t == "turn":
                turn2(g, p)
            if t == "toggle":
                toggle2(g, p)
    return sum([sum(x) for x in g])


print(part1())
# print(part2())
