import re


class Reindeer:

    def __init__(self, n, v, t, r):
        self.n = n
        self.v = int(v)
        self.t = int(t)
        self.r = int(r)

        self.x = [t, r]
        self.f = True
        self.d = 0

    def __repr__(self):
        return f"{self.n, self.v, self.t, self.r, self.d}"

    def fly1(self, s):
        d = 0
        while s > 0:
            d += self.v * min(self.t, s)
            s -= min(self.t, s)
            s -= self.r
        return d

    def __iter__(self):
        self.x = [self.t, self.r]
        self.f = True
        self.d = 0
        return self

    def __next__(self):
        if self.x[0] == 0 and self.f:
            self.x[0] = self.t
            self.f = False
        elif self.x[1] == 0 and not self.f:
            self.x[1] = self.r
            self.f = True

        if self.f:
            self.x[0] -= 1
            self.d += self.v
        else:
            self.x[1] -= 1

        return self.d


# PART 1
def part1():
    p = r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\." 
    r = []
    with open("input.txt") as f:
        for s in f.read().split('\n')[:-1]:
            r.append(Reindeer(*re.findall(p, s)[0]))
    return max(map(lambda x : x.fly1(2503), r))


# PART 2
def part2():
    p = r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."
    r = []
    with open("input.txt") as f:
        for s in f.read().split('\n')[:-1]:
            r.append(iter(Reindeer(*re.findall(p, s)[0])))

    points = [0 for i in range(len(r))]
    for _ in range(2503):
        x = [next(x) for x in r]
        m = max(x)
        for i in range(len(r)):
            if x[i] == m:
                points[i] += 1
    return max(points)


print(part1())
print(part2())
