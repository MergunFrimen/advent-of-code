def read():
    with open("input/08.txt") as f:
        return [[y.split() for y in x.split('|')] for x in f.read().rstrip().split('\n')]

def part1():
    m = read()
    print(sum(sum(map(lambda x : 1 if len(x) in [2,3,4,7] else 0, y)) for _, y in m))

def part2():
    translation = {
                   'abcefg' : 0,
                   'cf' : 1,
                   'acdeg' : 2,
                   'acdfg' : 3,
                   'bcdf' : 4,
                   'abdfg' : 5,
                   'abdefg' : 6,
                   'acf' : 7,
                   'abcdefg' : 8,
                   'abcdfg' : 9
                   }
    s = 0
    for display, output in read():
        segments = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[]}
        for digit in display:
            digit = [d for d in digit]
            if len(digit) == 2:
                segments['c'] += digit
                segments['f'] += digit
            if len(digit) == 3:
                segments['a'] += digit
                segments['c'] += digit
                segments['f'] += digit
            if len(digit) == 4:
                segments['b'] += digit
                segments['c'] += digit
                segments['d'] += digit
                segments['f'] += digit
            if len(digit) == 5:
                segments['a'] += digit
                segments['d'] += digit
                segments['g'] += digit
            if len(digit) == 6:
                segments['a'] += digit
                segments['b'] += digit
                segments['f'] += digit
                segments['g'] += digit
        for k, v in segments.items():
            segments[k] = [(v.count(i), i) for i in segments]
            segments[k] = list(filter(lambda x : x[0] == max(segments[k])[0], segments[k]))
        while sum(map(len, list(segments.values()))) != 7:
            for k in segments:
                if len(segments[k]) == 1:
                    l = segments[k][0][1]
                    for d in "abcdefg".replace(k, ''):
                        segments[d] = list(filter(lambda x : x[1] != l, segments[d]))
        for k, v in segments.items():
            segments[k] = v[0][1]
        
        result = {}
        n = ""
        for i, v in enumerate(segments.values()):
            result[v] = "abcdefg"[i]
        for digit in output:
            n += str(translation[''.join(sorted([result[d] for d in digit]))])
        s += int(n)
    print(s)

part1()
part2()
