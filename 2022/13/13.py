from itertools import permutations


def get_data():
    with open('input.txt') as f:
        return [list(map(eval, x.split())) for x in f.read().split('\n\n')]


def part1(data):
    correct = []
    for i, (left, right) in enumerate([(flatten(x), flatten(y)) for x, y in data]):
        if left == []:
            left = data[i][0]
        if right == []:
            right = data[i][1]
        if compare(left, right):
            correct += [i + 1]
    return sum(correct)


def compare(left, right):
    result = None

    for i in range(max(len(left), len(right))):
        if i == len(left):
            result = True
        elif i == len(right):
            result = False
        elif isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                result = True
            if left[i] > right[i]:
                result = False
        elif isinstance(left[i], list) and isinstance(right[i], list):
            result = compare(left[i], right[i])
        elif isinstance(left[i], int):
            result = compare([left[i]], right[i])
        else:
            result = compare(left[i], [right[i]])
        if result is not None:
            return result
    
    return None


def in_order(data):
    for i in range(0, len(data), 2):
        if not compare(data[i], data[i + 1]):
            return False
    return True


def part2(data):
    empty = []
    result = []
    data = [y for x in data for y in x] + [[[2]], [[6]]]

    for i in range(len(data)):
        y = flatten(data[i])
        if y == []:
            empty += [i]
        else:
            result += [y]
    
    result.sort()

    for x in permutations([data[i] for i in empty]):
        if in_order(list(x)):
            result = list(x) + result
            break
        
    return (result.index([2]) + 1) * (result.index([6]) + 1)


def flatten(data):
    result = []
    for x in data:
        if isinstance(x, list):
            result += flatten(x)
        else:
            result += [x]
    return result


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()