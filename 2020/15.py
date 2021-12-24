def read():
    return [int(n) for n in open("input/15.txt").read().rstrip().split(',')]

def part(count):
    m = read()
    pos = len(m)
    init = m[-1]
    memory = [0] * count

    for i, x in enumerate(m[:-1]):
        memory[x] = i + 1

    while pos <= count:
        if memory[init] == 0:
            initnew = 0
        else:
            initnew = pos - memory[init]
        memory[init] = pos
        init = initnew
        pos += 1

    return memory.index(count)

print(part(2020))
print(part(30000000))
