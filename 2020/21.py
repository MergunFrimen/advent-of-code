# --- Day 21: Allergen Assessment ---


from collections import Counter
import itertools as it


def solve_part1(data):
    all_ingredients = set()
    times = Counter()
    pos = {}

    for line in data:
        a, b = line.rstrip().split(" (contains ")
        ingredients = set(a.split())
        allergens = set(b[:-1].split(", "))
    
        all_ingredients |= ingredients
        times.update(ingredients)
    
        for alg in allergens:
            if alg not in pos:
                pos[alg] = ingredients.copy()
            else:
                pos[alg] &= ingredients
    
    bad = set(it.chain.from_iterable(pos.values()))
    return sum(times[food] for food in (all_ingredients - bad))


def solve_part2(data):
    pos = {}

    for line in data:
        a, b = line.rstrip().split(" (contains ")
        ingredients = set(a.split(" "))
        allergens = set(b[:-1].split(", "))
    
        for alg in allergens:
            if alg not in pos:
                pos[alg] = ingredients.copy()
            else:
                pos[alg] &= ingredients
    
    taken = set()
    items = []
    while True:
        for alg, ingredients in pos.items():
            if len(ingredients - taken) == 1:
                o = min(ingredients-taken)
                items.append((alg,o))
                taken.add(o)
                break
        else:
            break
    
    return ",".join(x[1] for x in sorted(items))


def read(filename):
    with open("input.txt", 'r') as f:
        return f.readlines()


def main():
    data = read("input.txt")
    solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    print(f"--- Part One ---\n{solution1}")
    print(f"--- Part Two ---\n{solution2}")


main()
