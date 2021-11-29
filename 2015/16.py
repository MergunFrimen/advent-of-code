# 1. parse into a matrix
# 2. find sues that match the mfcsam sue
# 3. return the number of the sue that matched the most fields (highest probability that it was her)

items = [
        "children:",
        "cats:",
        "samoyeds:",
        "pomeranians:",
        "akitas:",
        "vizslas:",
        "goldfish:",
        "trees:",
        "cars:",
        "perfumes:"
        ]

sue = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]


def read():
    with open("input.txt") as f:
        for x in f.read().split('\n')[:-1]:
            v = [-1 for _ in range(len(items))]
            x = x.split()
            for i in range(2, len(x), 2):
                v[items.index(x[i])] = int(x[i+1].rstrip(','))
            yield v


def part1(m):
    p = []
    for i in range(len(m)):
        x = 0
        for j in range(len(sue)):
            if m[i][j] != -1 and m[i][j] != sue[j]:
                break
            x += 1
        else:
            p.append((x, i+1))
    return sorted(p)[0]


def part2(m):
    p = []
    for i in range(len(m)):
        x = 0
        for j in range(len(m[i])):
            if m[i][j] != -1:
                if j in [1, 7] and m[i][j] > sue[j]:
                    x += 1
                elif j in [3, 6] and m[i][j] < sue[j]:
                    x += 1
                elif m[i][j] == sue[j]:
                    x += 1
                else:
                    break
        else:
            p.append((x, i+1))
    return sorted(p, reverse=True)[0]


print(part1(list(read())))
print(part2(list(read())))
