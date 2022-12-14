import heapq
from math import inf


def get_data():
    with open('input.txt') as f:
        data = [[y for y in x] for x in f.read().split()]
    s, e = None, None
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                s = (i, j)
                data[i][j] = 'a'
            if data[i][j] == 'E':
                e = (i, j)
                data[i][j] = 'z'
            data[i][j] = ord(data[i][j]) - 97
    return data, s, e 


def part1(data):
    heightmap, start, end = data
    distance = dijkstra(heightmap, start, end)
    return distance[end]


def valid(heightmap, pos):
    i, j = pos
    height, width = len(heightmap), len(heightmap[0])
    return 0 <= i < height and 0 <= j < width


def get_neighbors(heightmap, pos):
    result = []
    x, y = pos
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newx, newy = x + i, y + j
        if not valid(heightmap, (newx, newy)):
            continue
        if heightmap[x][y] + 1 >= heightmap[newx][newy]:
            result += [(newx, newy)]
    return result


def dijkstra(heightmap, start, end):
    distance = {start: 0}
    queue = [(distance[start], start)]
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if (i, j) != start:
                queue.append((inf, (i, j)))
                distance[(i, j)] = inf
    heapq.heapify(queue)

    while queue:
        _, (x, y) = heapq.heappop(queue)
        for i, j in get_neighbors(heightmap, (x, y)):
            if distance[(i, j)] > distance[(x, y)] + 1:
                distance[(i, j)] = distance[(x, y)] + 1
                heapq.heappush(queue, (distance[(i, j)], (i, j)))

    return distance


def part2(data):
    heightmap, start, end = data
    distances = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 0:
                distances += [dijkstra(heightmap, (i, j), end)[end]]
    return min(distances)


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()