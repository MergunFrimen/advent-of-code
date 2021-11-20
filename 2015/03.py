def sum_tuple(x, y):
    return x[0] + y[0], x[1] + y[1]


# PART 1
def part1():
    dirs = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    santa_pos = [(0, 0)]
    with open("input.txt", "r") as f:
        for d in list(f.read()[:-1]):
            santa_pos.append(sum_tuple(santa_pos[-1], dirs[d]))
    return len(set(santa_pos))


# PART 2
def part2():
    dirs = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    santa_pos, robot_pos= [(0, 0)], [(0, 0)]
    with open("input.txt", "r") as f:
        for i, d in enumerate(list(f.read()[:-1])):
            if i % 2 == 0:
                santa_pos.append(sum_tuple(santa_pos[-1], dirs[d]))
            if i % 2 == 1:
                robot_pos.append(sum_tuple(robot_pos[-1], dirs[d]))
    return len(set(santa_pos) | set(robot_pos))


print(part1())
print(part2())
