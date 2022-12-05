import math
import heapq

def read():
    with open("input/15.txt") as f:
        return [[int(x) for x in row] for row in f.read().split()]

def larger():
    m = read()
    new = [[m[i % len(m)][j % len(m)] for i in range(5 * len(m))] for j in range(5 * len(m))]
    for i in range(len(new)):
        for j in range(len(new)):
            new[i][j] += i // len(m) + j // len(m[0])
            if new[i][j] >= 10:
                new[i][j] -= 9
    return new

def neighboors(m, n):
    for x, y in [(n[0]+a, n[1]+b) for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
        if len(m) > x >= 0 and len(m) > y >= 0:
            yield (x,y)

def part(m):
    heap = []
    dist, prev = {}, {}
    
    # initialize
    for i in range(len(m)):
        for j in range(len(m)):
            dist[(i, j)] = math.inf
            prev[(i, j)] = None
            if (i, j) == (0, 0):
                dist[(i, j)] = 0
            heap.append((dist[(i, j)], (i, j)))
    heapq.heapify(heap)

    # dijkstra
    while heap:
        _, u = heapq.heappop(heap)
        for n in list(neighboors(m, u)):
            i, j = n
            alt = dist[u] + m[i][j]
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
                heapq.heappush(heap, (dist[n], n))

    print(dist[len(m) - 1, len(m) - 1])

part(read())
part(larger())
