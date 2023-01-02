from re import findall

EMPTY = ' '
OPEN = '.'
WALL = '#'

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
DIRECTIONS = {RIGHT: (0, 1), DOWN: (1, 0), LEFT: (0, -1), UP: (-1, 0)}


def get_data():
    with open('input.txt') as f:
        plan, move = f.read().split('\n\n')
    plan = [[y for y in row] for row in plan.split('\n')]
    max_width = max(len(row) for row in plan)
    plan = [row + [' '] * (max_width - len(row)) for row in plan]
    move = [x if x in 'LR' else int(x) for x in findall('\d+|[RL]', move)]
    return plan, move


def wrap(plan, position):
    x, y = position
    width, height = len(plan[0]), len(plan)
    return x % height, y % width


def is_blocked(plan, position, direction):
    return position == get_next_position(plan, position, direction)


def move(plan, position, direction):
    x, y = get_next_position(plan, position, direction)

    while plan[x][y] == EMPTY:
        if is_blocked(plan, (x, y), direction):
            return position
        x, y = get_next_position(plan, (x, y), direction)
    
    return x, y


def get_next_position(plan, position, direction):
    i, j = position
    x, y = DIRECTIONS[direction]
    i, j = wrap(plan, (x + i, y + j))
    if plan[i][j] == WALL:
        return position
    return i, j


def turn(direction, m):
    t = {'R': 1, 'L': -1}
    return (direction + t[m]) % 4


def part1(data):
    plan, moves = data
    x, y, direction = 0, plan[0].index(OPEN), RIGHT
    
    for m in moves:
        if isinstance(m, str):
            direction = turn(direction, m)
        else:
            for _ in range(m):
                x, y = move(plan, (x, y), direction)
    
    # for i in range(len(plan)):
    #     for j in range(len(plan[i])):
    #         if (i, j) == (x, y):
    #             print('O', sep='', end='')
    #         else:
    #             print(plan[i][j], sep='', end='')
    #     print()
    
    return 1000 * (x + 1) + 4 * (y + 1) + direction



def part2(data):
    return


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()