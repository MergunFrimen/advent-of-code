def is_nice1(s):
    bitmap = [3, 1]
    vowels = "aeiou"
    illegal = ['ab', 'cd', 'pq', 'xy']
    previous = ''

    for l in s:
        if previous+l in illegal:
            return False
        if l in vowels:
            bitmap[0] -= 1
        if l == previous:
            bitmap[1] -= 1
        previous = l

    return max(bitmap) <= 0


def is_nice2(s):
    bitmap = [False, False]
    for i in range(len(s)):
        if s[i:i+2] in s[i+2:]:
            bitmap[0] = True
        if s[i:i+1] == s[i+2:i+3]:
            bitmap[1] = True
    return min(bitmap)


# PART 1
def part1():
    with open("input.txt", "r") as f:
        for s in f.read().split():
            yield is_nice1(s)


# PART 2
def part2():
    with open("input.txt", "r") as f:
        for s in f.read().split():
            yield is_nice2(s)


print(sum(part1()))
print(sum(part2()))
