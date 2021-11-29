def part1(s, x):
    for _ in range(x):
        p, r = s[0], []
        i = 1
        for x in s[1:]:
            if x == p:
                i += 1
            else:
                r += [i, p]
                i, p = 1, x
        s = ''.join(map(str, r + [i, p]))
    return len(s)


def part2(s, x):
    return part1(s, x)


input_num = "1113122113"
print(part1(input_num, 40))
print(part2(input_num, 50))
