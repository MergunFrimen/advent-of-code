# from _ import _


def get_data():
    with open('input.txt') as f:
        return dict([x.split(': ') for x in f.read().split('\n')[:-1]])


def part1(data):
    return int(rec(data, 'root'))


def rec(data, current):
    if ' ' not in data[current]:
        return int(data[current])
    
    left, op, right = data[current].split(' ')
    left = rec(data, left)
    right = rec(data, right)

    return eval(f'{left} {op} {right}')


def rec2(data, current):
    if current == 'humn':
        return 'humn'
    if ' ' not in data[current]:
        return data[current]
    
    left, op, right = data[current].split(' ')
    left = rec2(data, left)
    right = rec2(data, right)

    return f'({left} {op} {right})'


def part2(data):
    left, _ , right = data['root'].split(' ')
    left, right = rec2(data, left), rec2(data, right)
    
    if 'humn' in left:
        equation, other = left, right
    else:
        equation, other = right, left
    
    number = flipper(equation, other)
    assert eval(f'{equation.replace("humn", str(number))} == {other}')

    return int(number)


def flipper(equation, other):
    if 'humn' == equation:
        return eval(other)

    equation = equation[1:-1]
    stack = []
    i = 0
    for i, x in enumerate(equation):
        if x == '(':
            stack.append(x)
        elif x == ')':
            stack.pop()
        elif not stack and x in '+-*/':
            break

    left, op, right = equation[:i-1], opposite(equation[i]), equation[i+2:]
    if 'humn' in left:
        other = f'({other} {op} {right})'
        return flipper(left, other)
    if 'humn' in right:
        if equation[i] in '-/':
            other = f'({left} {equation[i]} {other})'
        else:
            other = f'({other} {op} {left})'
        return flipper(right, other)
    

def opposite(op):
    dict = {
        '/': '*',
        '*': '/',
        '-': '+',
        '+': '-',
    }
    return dict[op]


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()