from typing import Dict, List, Tuple
import re


class Bag:

    def __init__(self, name: str, bags: List['Bag']):
        self.name = name
        self.bags = bags


def parse(raw: str) -> Dict[str, Bag]:

    regex = r"([a-z ]+) bags contain (.+)."
    bags = dict()

    # Initial dictionary creation
    for bag, contents in re.findall(regex, raw):
        bags[bag] = Bag(bag, fill_bag(contents))

    # Connects the bags
    for bag in bags.values():
        bag.bags = [(int(x[0]), bags[x[1]]) for x in bag.bags]

    return bags


def fill_bag(contents: List[str]) -> List[Tuple[int, str]]:

    # Skip these
    if contents == "no other bags":
        return []

    bag_list = []

    # Create tuples for bag list
    for x in contents.split(', '):
        amount = int(x.split()[0])
        bag_name = " ".join(x.split()[1:-1])
        bag_list.append((amount, bag_name))

    return bag_list



def search(bag: Bag, amount: int, level: int=0):

    if level != 0 and bag.name == "shiny gold":
        return True

    # print("  " * level, amount, bag.name)

    for n, x in bag.bags:
        if search(x, n, level + 1):
            return True

    return False


def count_bags(bag, amount, level=0):

    counter = 1

    for n, x in bag.bags:
        counter += n * count_bags(x, n, level + 1)

    return counter


def main():

    with open('input.txt', 'r') as f:
        raw: str = f.read()
    
    # {bagcolor: Bag} dictionary
    bags = parse(raw)

    shiny_bag_counter = 0
    bag_req_counter = 0

    for bag in bags.values():
        if search(bag, 1):
            shiny_bag_counter += 1

    bag_req_counter = count_bags(bags["shiny gold"], 1)

    print("--- Part One ---\n", shiny_bag_counter)
    print("--- Part Two ---\n", bag_req_counter)


main()
