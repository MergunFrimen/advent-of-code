# PART 1
def part1():
    values = dict()
    with open("input.txt", "r") as f:
        wires = [l.split() for l in f.read().split('\n')[:-1]]
    for w in wires:
        if len(w) == 3 and w[0].isdigit():
            values[w[2]] = w[0]

    for w in wires:

print(part1())
