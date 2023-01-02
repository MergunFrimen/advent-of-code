# from _ import _


def get_data():
    with open('input.txt') as f:
        return list(map(int, f.read().split()))


def part1(data):
    n = len(data)
    m = list(range(n))
    p = list(range(n))

    for _ in range(1):
        for i in range(n):
            i = m[i]
            if data[i] < 0:
                negative = True
                v = data[i] % n - n
            else:
                negative = False
                v = data[i] % n
            if negative:
                for _ in range(abs(v)):
                    p[i], p[i-1] = p[i-1], p[i]

            



def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()