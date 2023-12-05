import os 
import re


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/input.txt') as f:
        data = f.read().split('\n')
        result = []
        cut = [line.split(': ')[1] for line in data]
        result = [x.split(', ') for x in cut.split('; ')]
        result = [[x.split(' ') for x in y] for y in result]
        return result
            

def part1(data):
    print(data)

def part2(data):
    pass


def main():
    print(f'part1: {part1(get_data())}')
    # print(f'part2: {part2(get_data())}')

main()