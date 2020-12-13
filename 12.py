#!/usr/bin/env python3

# --- Day 12: Rain Risk --- #


class Ship:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x_axis = x
        self.y_axis = y

    def __str__(self):
        return "Ship({}, ({},{}))".format(self.direction, self.x_axis, self.y_axis)


def read(filename):
    with open(filename, 'r') as f:
        instructions = [(x[0], int(x[1:-1])) for x in f]
    return instructions


def solve_part1(instructions):
    ship = Ship('E', 0, 0)
    for action, amount in instructions:
        execute(ship, action, amount)
    return abs(ship.x_axis) + abs(ship.y_axis)


def execute(ship, action, amount):
    if action == 'N':
        ship.y_axis += amount
    elif action == 'S':
        ship.y_axis -= amount
    elif action == 'E':
        ship.x_axis += amount
    elif action == 'W':
        ship.x_axis -= amount
    elif action == 'L':
        ship.direction = rotate(ship, action, amount)
    elif action == 'R':
        ship.direction = rotate(ship, action, amount)
    elif action == 'F':
        execute(ship, ship.direction, amount)


def rotate(ship, action, amount):
    assert action == 'L' or action == 'R', action
    if action == 'L':
        directions = ['E', 'N', 'W', 'S']
    if action == 'R':
        directions = ['E', 'S', 'W', 'N']
    offset = directions.index(ship.direction)
    return directions[(amount // 90 + offset) % 4]


def solve_part2(instructions):
    ship = Ship("", 0,0)
    waypoint = Ship("", 10, 1)
    for action, amount in instructions:
        execute2(ship, waypoint, action, amount)
        print(ship, waypoint)
    return abs(ship.x_axis) + abs(ship.y_axis)


def execute2(ship, waypoint, action, amount):
    if action == 'N':
        waypoint.y_axis += amount
    elif action == 'S':
        waypoint.y_axis -= amount
    elif action == 'E':
        waypoint.x_axis += amount
    elif action == 'W':
        waypoint.x_axis -= amount

    elif action == 'L':
        rotate2(waypoint, action, amount)
    elif action == 'R':
        rotate2(waypoint, action, amount)
    elif action == 'F':
        ship.x_axis += amount * waypoint.x_axis
        ship.y_axis += amount * waypoint.y_axis


def rotate2(waypoint, action, amount):
    assert action == 'L' or action == 'R', action
    if action == 'L':
        for _ in range(amount // 90):
            waypoint.x_axis, waypoint.y_axis = waypoint.y_axis * -1, waypoint.x_axis
    if action == 'R':
        for _ in range(amount // 90):
            waypoint.x_axis, waypoint.y_axis = waypoint.y_axis, waypoint.x_axis * -1



def main():
    instructions = read('input.txt')
    solution1 = solve_part1(instructions)
    solution2 = solve_part2(instructions)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
