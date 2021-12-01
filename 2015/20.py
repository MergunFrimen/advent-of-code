def part1(t):
    s = 0
    x = 0
    while s < t:
        s = 0
        x += 1
        for i in range(1, x+1):
            if t % i == 0:
                s += 10 * i
        print(s)
    return x


print(part1(33100000))
print(part1(130))
