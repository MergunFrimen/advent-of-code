

WIN = {'A': 'Y', 'B': 'Z', 'C': 'X'}
DRAW = {'A': 'X', 'B': 'Y', 'C': 'Z'}
LOSE = {'A': 'Z', 'B': 'X', 'C': 'Y'}
SCORING = {'X': 1, 'Y': 2, 'Z': 3}


def get_data():
    with open('input.txt') as f:
        return [x.split() for x in f.read().split('\n')][:-1]


def part1(data):
    score = 0
    for opponent, my in data:
        score += SCORING[my]
        if DRAW[opponent] == my:
            score += 3
        elif WIN[opponent] == my:
            score += 6
    return score


def part2(data):
    score = 0
    for opponent, my in data:
        if my == 'X':
            score += SCORING[LOSE[opponent]]
        elif my == 'Y':
            score += SCORING[DRAW[opponent]] + 3
        elif my == 'Z':
            score += SCORING[WIN[opponent]] + 6
    return score


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()