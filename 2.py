from typing import List, Tuple


def filter_valid(filename: str) -> List[Tuple[str, str]]:

    f = open(filename, 'r')
    input_rules = f.read().split('\n')
    valid_input = []

    # Check all rules
    for x in input_rules:

        if x == '':
            continue

        rule = x.split(':')[0]
        passwd = x.split(':')[1][1:]

        if check2(rule, passwd):
            valid_input.append((rule, passwd))

    return valid_input


def check1(rule: str, passwd: str) -> bool:

    amount = rule.split(' ')[0]
    letter = rule.split(' ')[1]

    at_least = int(amount.split('-')[0])
    at_most = int(amount.split('-')[1])

    return at_least <= passwd.count(letter) <= at_most


def check2(rule: str, passwd: str) -> bool:

    amount = rule.split(' ')[0]
    letter = rule.split(' ')[1]

    low_index = int(amount.split('-')[0]) - 1
    high_index = int(amount.split('-')[1]) - 1

    return (passwd[low_index]  == letter and not passwd[high_index] == letter)or \
           (passwd[high_index] == letter and not passwd[low_index]  == letter)




print(len(filter_valid('input.txt')))
