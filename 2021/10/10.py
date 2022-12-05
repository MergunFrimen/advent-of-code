score = {
         ')': 3,
         ']': 57,
         '}': 1197,
         '>': 25137
         }
score2 = {
         ')': 1,
         ']': 2,
         '}': 3,
         '>': 4 
         }
opening = "([{<"
closing = ")]}>"

def read():
    with open("input/10.txt") as f:
        return [[l for l in x] for x in f.read().split()]

def part1():
    m = read()
    corrupted = []
    s = 0
    for i, row in enumerate(m):
        stack = []
        for p in row:
            if p in opening:
                stack.append(p)
            elif p in closing:
                x = stack.pop()
                if opening.index(x) != closing.index(p):
                    s += score[p]
                    corrupted.append(i)
                    break
    print(s)
    return [x for i, x in enumerate(m) if i not in corrupted] 

def part2():
    m = part1()
    scores = []
    for row in m:
        stack = []
        for p in row:
            if p in opening:
                stack.append(p)
            elif p in closing:
                x = stack.pop()
        s = 0
        for x in stack[::-1]:
            s = 5*s + score2[closing[opening.index(x)]]
        scores.append(s)
    print(list(sorted(scores))[len(scores) // 2])

part2()
