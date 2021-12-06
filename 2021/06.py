def read():
    with open("input.txt") as f:
        return [int(x) for x in f.read().rstrip().split(',')]

def part(iterations):
    a = [read().count(i) for i in range(9)]
    for _ in range(iterations):
        x0 = a[0]
        a = a[1:] + [x0]
        a[6] += x0
    print(sum(a))

part(80)
part(256)
