import time
from heapq import heappop, heappush

def get_neighbors(lines, node):
    neighbors = []
    node_height = lines[node[0]][node[1]]
    for i in range(1, -2, -2):
        if i == 0:
            continue
        if 0 <= node[0] + i < len(lines) and (tmp := (node[0] + i, node[1])) and (lines[tmp[0]][tmp[1]] - node_height) > -2:
            neighbors.append(tmp)

        if 0 <= node[1] + i < len(lines[0]) and (tmp := (node[0], node[1] + i)) and (lines[tmp[0]][tmp[1]] - node_height) > -2:
            neighbors.append(tmp)

    return neighbors


def dijkstra(lines, start, dest):
    if stage == 2:
        destinations = [(i,j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == 1]
    else:
        destinations = [dest]

    unvisited = []
    visited = set()
    current = (0, start) #distance, currNode
    heappush(unvisited, current)
    while len(unvisited) != 0:
        current_dist, current_node = heappop(unvisited)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node in destinations:
            print("shortest path:", current_dist)
            break

        for n in get_neighbors(lines, current_node):
            heappush(unvisited, (current_dist + 1, n))


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = [[c for c in line.strip()] for line in input_file.readlines()]
    endpos = None
    startpos = None

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                lines[i][j] = 1
                startpos = (i, j)
                continue
            if c == 'E':
                lines[i][j] = 26
                endpos = (i, j)
                continue
            lines[i][j] = ord(c) - 0x60

    dijkstra(lines, endpos, startpos)


if __name__ == '__main__':
    testing = False
    stage = 1
    start = time.time()
    task()
    print(time.time() - start)
    stage = 2
    start = time.time()
    task()
    print(time.time() - start)
