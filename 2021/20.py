def read():
    with open("input/20.txt") as f:
        algo, imag = f.read().rstrip().split('\n\n')
    return algo, [[i for i in row] for row in imag.split()]

def double_size(m, t):
    new = [t for _ in range(len(m))]
    m = [new + row + new for row in m]
    new += m

def part1():
    algo, imag = read()

def part2():
    m = read()

part1()
part2()
