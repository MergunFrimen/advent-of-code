def is_valid(p):
    return legal(p) and straight(p) and pairs(p)


def straight(p):
    for i in range(len(p) - 2):
        if ord(p[i]) + 2 == ord(p[i+1]) + 1 == ord(p[i+2]):
            return True
    return False


def legal(p):
    for i in range(len(p)):
        if p[i] in {'o', 'i', 'l'}:
            p[i] = chr(ord(p[i]) + 1)
            for j in range(i+1, len(p)):
                p[j] = 'a'
            return False
    return True 


def pairs(p):
    x = ''.join(p)
    i, c = 0, 0
    while i < len(p) - 1:
        if p[i] == p[i+1]:
            c += 1
            i += 1
        i += 1
    return c >= 2


def inc(p):
    i = 7
    p[i] = chr(ord(p[i]) + 1)
    while ord(p[i]) > ord('z') and i >= 0:
        p[i] = 'a'
        i -= 1
        p[i] = chr(ord(p[i]) + 1)
    if i < 0:
        p[i] = 'a'
    return p


# PART 1 & 2
def part1(p):
    p = [x for x in p]
    while True:
        p = inc(p)
        if is_valid(p):
            return ''.join(p)
    return None


input_num = "vzbxkghb"
print(part1(part1(input_num)))
