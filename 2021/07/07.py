with open("input/07.txt") as f:
    m = [int(x) for x in f.read().rstrip().split(',')]
print(min((sum(abs(y - x) for y in m), x) for x in range(max(m))))
print(min((sum(sum(range(1, abs(y - x) + 1)) for y in m), x) for x in range(max(m))))
