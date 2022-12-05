EAST, SOUTH, EMPTY = '>', 'v', '.'

def read():
    with open("input/25.txt") as f:
        return [[x for x in row] for row in f.read().rstrip().split()]

def swap(m, to_move):
    for (i, j), (x, y) in to_move:
        m[i][j], m[x][y] = m[x][y], m[i][j]

def move_east(m):
    to_move = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == EAST and m[i][(j + 1) % len(m[0])] == EMPTY:
                to_move.append(((i, j), (i, (j + 1) % len(m[0]))))
    swap(m, to_move)
    return len(to_move) 

def move_south(m):
    to_move = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == SOUTH and m[(i + 1) % len(m)][j] == EMPTY:
                to_move.append(((i, j), ((i + 1) % len(m), j)))
    swap(m, to_move)
    return len(to_move) 

def move(m):
    s = 0
    s += move_east(m)
    s += move_south(m)
    return s

def part1():
    m = read()
    i = 0
    while True:
        i += 1
        if not move(m):
            break
    print(i)

part1()
