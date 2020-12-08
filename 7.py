import re
from typing import Dict, List


class Bag:

    def __init__(self, name, bags):
        self.name = name
        self.bags = bags


def parse(raw):

    bags = dict()
    regex = r"([a-z ]+) bags contain (.+)."

    # Initial dictionary creation
    for bag, contents in re.findall(regex, raw):
        bags_list = [(x.split()[0], " ".join(x.split()[1:-1])) for x in contents.split(', ') if x != "no other bags"]
        bags[bag] = Bag(bag, bags_list)

    # Connects the bags
    for bag in bags.values():
        bag.bags = [(int(x[0]), bags[x[1]]) for x in bag.bags]


    return bags


def search(bag, name, amount, level=0):

    if level != 0 and bag.name == name:
        return True

    print("  " * level, amount, bag.name)

    for n, x in bag.bags:
        if search(x, name, n, level + 1):
            return True

    return False


def count_bags(bag, amount, lst, level=0):

    counter = 1

    for n, x in bag.bags:
        counter += n * count_bags(x, n, lst, level + 1)

    return counter


def part1():

    with open('input.txt', 'r') as f:
        raw: str = f.read()

    bags: Dict[str, Bag] = parse(raw)
    counter = 0

    for bag in bags.values():
        if search(bag, "shiny gold", 1):
            counter += 1

    print(counter)


def part2():

    with open('input.txt', 'r') as f:
        raw: str = f.read()

    bags: Dict[str, Bag] = parse(raw)
    amounts: Dict[str]

    lst = []
    print(count_bags(bags["shiny gold"], 1, lst))


part2()
