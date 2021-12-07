def read():
    with open("input/04.txt") as f:
        l = f.read().split('\n\n')
    numbers = [x for x in l[0].split(',')]
    boards = [b.split() for b in l[1:]]
    return numbers, boards

def cross_out(boards, n):
    for b in boards:
        for i in range(25):
            if b[i] == n:
                b[i] = '*' + b[i]
     
def check(boards):
    for b in boards:
        rows = [[b[5*i + j] for j in range(5)] for i in range(5)]
        cols = [[b[5*i + j] for i in range(5)] for j in range(5)]
        for r in rows:
            if not list(filter(lambda x : "*" not in x, r)):
                return b
        for c in cols:
            if not list(filter(lambda x : "*" not in x, c)):
                return b
    return None

def check2(boards):
    remove = []
    for b in boards:
        rows = [[b[5*i + j] for j in range(5)] for i in range(5)]
        cols = [[b[5*i + j] for i in range(5)] for j in range(5)]
        for r in rows:
            if not list(filter(lambda x : "*" not in x, r)) and b not in remove:
                remove.append(b)
        for c in cols:
            if not list(filter(lambda x : "*" not in x, c)) and b not in remove:
                remove.append(b)
    return remove

def board_sum(b):
    return sum(map(int, filter(lambda x : '*' not in x, b)))

def part1(m):
    numbers, boards = m
    for n in numbers:
        cross_out(boards, n)
        b = check(boards)
        if b is not None:
            return board_sum(b) * int(n)
    print("ERROR")

def part2(m):
    numbers, boards = m
    for n in numbers:
        cross_out(boards, n)
        remove = check2(boards)
        if len(remove) == 1 and len(boards) == 1:
            return board_sum(remove[0]) * int(n)
        for b in remove:
            boards.remove(b)
    print("ERROR")

print(part1(read()))
print(part2(read()))
