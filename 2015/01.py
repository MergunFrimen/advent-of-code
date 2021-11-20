# PART1
with open("input.txt", "r") as f:
    x = f.read()
    print(x.count('(') - x.count(')'))


# PART 2
with open("input.txt", "r") as f:
    s = 0
    for i, x in enumerate(f.read()):
        if x == '(':
            s += 1
        else:
            s -= 1
        if s == -1:
            print(i + 1)
            break
