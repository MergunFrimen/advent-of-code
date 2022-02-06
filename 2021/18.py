import math

def read():
    with open("input/18.txt") as f:
        return [[x for x in line] for line in f.read().split()]

# NOTE: could be done with recursion and a tree structure
def explode(m):
    d = 0
    for i, x in enumerate(m):
        if x == '[':
            d += 1
        elif x == ']':
            d -= 1
        if d >= 5:
            j = i
            while m[j] != ']':
                j += 1
            l, r = m[i+1], m[i+3]
            m[i:j+1] = '0'
            j = i
            while i > 0:
                i -= 1
                if m[i].isdigit():
                    m[i] = str(int(m[i]) + int(l))
                    break
            while j < len(m) - 1:
                j += 1
                if m[j].isdigit():
                    m[j] = str(int(m[j]) + int(r))
                    break
            return True
    return False

def split(m):
    for i, x in enumerate(m):
        if x.isdigit() and int(x) > 9:
            l, r = math.floor(int(x)/2), math.ceil(int(x)/2)
            m[:] = m[:i] + ['[',str(l),',',str(r),']'] + m[i+1:]
            return True
    return False

def correct(m):
    while True:
        if explode(m):
            continue
        if split(m):
            continue
        break

def addition(m):
    result = m.pop(0)
    while m:
        result = add_numbers(result, m.pop(0))
        correct(result)
    return eval(''.join(result))

def add_numbers(m1, m2):
    return ['['] + m1 + [','] + m2 + [']']

def magnitude(m):
    if not isinstance(m, list):
        return m
    return 3*magnitude(m[0]) + 2*magnitude(m[1])

def largest_magnitude(m):
    result = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                m1 = magnitude(addition([m[i]] + [m[j]]))
                m2 = magnitude(addition([m[j]] + [m[i]]))
                result = max(result, m1, m2)
    return result

def part1():
    m = read()
    print(magnitude(addition(m)))

def part2():
    m = read()
    print(largest_magnitude(m))

part1()
part2()
