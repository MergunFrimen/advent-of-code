#!/usr/bin/env python3

from typing import List, Tuple


class Tiles:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.tiles = []
        self.ref_tile = (0, 0)

    def create(self):
        self.tiles = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.ref_tile = (self.height // 2, self.width // 2)

    def __repr__(self) -> str:
        result = 'Tiles:\n'
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.tiles[i][j])
            result += '\n'
        return result

    def count_black(self) -> int:
        return sum([1 for row in self.tiles for x in row if x == 1])


def solve_part1(data: List[List[str]]) -> int:

    tiles = Tiles(1000, 1000)
    tiles.create()
    flip(tiles, data)

    return tiles.count_black()


def flip(tiles: Tiles, data: List[List[str]]):
 
    #      0  1   2
    #    0    nw
    #    1 w      ne
    #    2    rf  
    #    3 sw     e
    #    4    se
    # 
   
    for row in data:
        curr_tile = tiles.ref_tile

        for tile in row:
            if tile == 'e':
                curr_tile = move(curr_tile, 1, 1)
            elif tile == 'w':
                curr_tile = move(curr_tile, -1, -1)
            elif tile == 'se':
                curr_tile = move(curr_tile, 2, 0)
            elif tile == 'nw':
                curr_tile = move(curr_tile, -2, 0)
            elif tile == 'ne':
                curr_tile = move(curr_tile, -1, 1)
            elif tile == 'sw':
                curr_tile = move(curr_tile, 1, -1)

        if not bounded(tiles, curr_tile):
            print("not bounded")

        i, j = curr_tile
        tiles.tiles[i][j] = (tiles.tiles[i][j] + 1) % 2


def move(tile: Tuple[int, int], x: int, y: int) -> Tuple[int, int]:
    return (tile[0] + x, tile[1] + y)


def bounded(tiles: Tiles, tile: Tuple[int, int]) -> bool:
    return tile[0] <= tiles.height and tile[1] <= tiles.width


def solve_part2(data: List[List[str]]) -> int:

    tiles = Tiles(1000, 1000)
    tiles.create()
    flip(tiles, data)

    for _ in range(100):
        print(tiles.count_black())
        repeat(tiles)

    return tiles.count_black()


def repeat(tiles: Tiles) -> None:

    to_flip = []
    for i in range(2, tiles.height - 2):
        for j in range(1, tiles.width - 1):
            if surrounding(tiles, i, j):
                to_flip.append((i, j))

    for i, j in to_flip:
        tiles.tiles[i][j] = (tiles.tiles[i][j] + 1) % 2


def surrounding(tiles, i, j):
    
    e  = tiles.tiles[i + 1][j + 1]
    w  = tiles.tiles[i - 1][j - 1]
    se = tiles.tiles[i + 2][j + 0]
    nw = tiles.tiles[i - 2][j + 0]
    ne = tiles.tiles[i - 1][j + 1]
    sw = tiles.tiles[i + 1][j - 1]
    
    blacks = sum([e, w, se, nw, ne, sw])
    if tiles.tiles[i][j] == 1 and (blacks == 0 or blacks > 2):
        return True
    if tiles.tiles[i][j] == 0 and (blacks == 2):
        return True

    return False


def parse(filename: str) -> List[List[str]]:

    with open(filename, 'r') as f:
        data = f.read()[:-1].split()

    for i, row in enumerate(data):
        temp = []
        while row:
            if row[:2] not in ['ne', 'se', 'sw','nw']:
                x = row[0]
                row = row[1:]
            else:
                x = row[:2]
                row = row[2:]
            temp.append(x)
        data[i] = temp

    return data


def main() -> None:

    data = parse('input.txt')
    # solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    # print(f"--- Part One ---\n{solution1}") 
    print(f"--- Part Two ---\n{solution2}") 


main()
