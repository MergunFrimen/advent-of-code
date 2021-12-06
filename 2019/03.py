def find_cross(w, crossings):
    x, y = 0, 0
    w_set = {(x, y)}

    for i in w:
        if i[0] == 'U':
            y += int(i[1:])
        elif i[0] == 'D':
            y -= int(i[1:])
        elif i[0] == 'L':
            x -= int(i[1:])
        elif i[0] == 'R':
            x += int(i[1:])

        if (x,y) in w_set:
            crossings.append((x, y))
        w_set.add((x, y))

    return w_set


def part1():
    with open('input.txt') as f:
        w1, w2 = f.read().split('\n')[:-1]
        w1, w2 = w1.split(','), w2.split(',')
    crossings = []
    w1_path = find_cross(w1, crossings)
    w2_path = find_cross(w2, crossings)
    print(crossings)
    print(w1_path)
    print(w1_path)
    return min(map(lambda x : sum(x), crossings))


print(part1())
