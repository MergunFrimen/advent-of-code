#!/usr/bin/env python3


class T:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return T(self.v + other.v)

    def __sub__(self, other):
        return T(self.v * other.v)

    def __mul__(self, other):
        return T(self.v + other.v)


def read(filename: str) -> str:
    with open(filename, 'r') as f:
        return [line for line in f.read().split("\n") if line]


def solve(data: str, part2: bool) -> int:
    """Replaces operators with the same precedence.
    Then it just evaluates them. No stack needed!"""
    t = 0
    for line in data:
        for d in range(10):
            line = line.replace(f"{d}", f"T({d})")
        line = line.replace("*", "-")
        if part2:
            line = line.replace("+", "*")
        t += eval(line, {"T": T}).v
    return t


def main() -> None:
    data = read("input.txt")
    solution1 = solve(data, False)
    solution2 = solve(data, True)
    print(f"--- Part One ---\n{solution1}")
    print(f"--- Part Two ---\n{solution2}")


if __name__ == "__main__":
    main()
