import time
import numpy as np
from heapq import heappop, heappush

def get_neighbors(lines, node, unvisited):
    neighbors = []
    for i in range(1, -2, -2):
        if i == 0:
            continue
        if 0 <= node[0] + i < len(lines) and (tmp := (node[0] + i, node[1])) in unvisited:
            neighbors.append(tmp)

        if 0 <= node[1] + i < len(lines[0]) and (tmp := (node[0], node[1] + i)) in unvisited:
            neighbors.append(tmp)

    return neighbors

def get_smallest(distances, unvisited):
    min_dist = np.inf
    min_node = unvisited[0]
    for node in unvisited:
        if (dist := distances.get(node)) < min_dist:
            min_dist = dist
            min_node = node

    return min_node

def get_smallest_i(todos):
    min_dist = todos[0][0]
    min_index = 0
    for i, node in enumerate(todos):
        if (dist := todos[i][0]) < min_dist:
            min_dist = dist
            min_index = i

    return min_index

def basic_dijkstra(lines):
    unvisited = [(x, y) for x in range(len(lines[0])) for y in range(len(lines))]
    print(unvisited)
    distances = {node: np.inf for node in unvisited}

    init_node = unvisited[0]  # (0,0)
    dest_node = (len(lines) - 1, len(lines[0]) - 1)
    distances[init_node] = 0

    current = init_node
    paths = {current: []}
    while True:
        current_dist = distances[current]
        for neighbor in get_neighbors(lines, current, unvisited):
            new_dist = current_dist + lines[neighbor[0]][neighbor[1]]
            if new_dist < distances.get(neighbor):
                distances[neighbor] = new_dist
                tmp_path = paths.get(current, []).copy()
                tmp_path.append(current)
                paths[neighbor] = tmp_path

        unvisited.remove(current)
        if dest_node not in unvisited:
            [print(p, distances[p]) for p in paths[dest_node]]
            print(dest_node, distances[dest_node])
            break

        current = get_smallest(distances, unvisited)

    return paths[dest_node]

def make_move(lines, unvisited, current, direction):
    neighbor = (current[1][0]+direction[0], current[1][1]+direction[1])
    if neighbor[0] < 0 or neighbor[0] >= len(lines) or neighbor[1] < 0 or neighbor[1] >= len(lines[0]):  # oob
        return

    new_dist = current[0] + lines[neighbor[0]][neighbor[1]]
    if all(direction[i] == current[2][i] for i in range(2)) or all(c == 0 for c in current[2]):  # same direction mate
        if current[3] < (3 if stage == 1 else 10):
            #unvisited.append((new_dist, neighbor, direction, current[3] + 1))
            heappush(unvisited, (new_dist, neighbor, direction, current[3] + 1))
        return

    if not all(direction[i] == -current[2][i] for i in range(2)):  # would go back
        if stage == 2 and current[3] < 4:
            return
        #unvisited.append((new_dist, neighbor, direction, 1))
        heappush(unvisited, (new_dist, neighbor, direction, 1))

def dijkstra_aoc(lines):
    nodes = [(x, y) for x in range(len(lines[0])) for y in range(len(lines))]

    init_node = nodes[0]  # (0,0)
    dest_node = (len(lines) - 1, len(lines[0]) - 1)

    unvisited = []
    visited = set()
    current = (0, init_node, (0, 0), 0) #Loss, currNode, direction, directionCount
    heappush(unvisited, current)
    #unvisited.append(current)

    while len(unvisited) != 0:
        #current = unvisited.pop(get_smallest_i(unvisited))
        current = heappop(unvisited)

        visited_node = (current[1], current[2], current[3])
        if visited_node in visited:
            continue

        visited.add(visited_node)

        if current[1] == dest_node:
            print(f"Stage {stage}: {current[0]}")
            break

        for i in range(1, -2, -2):
            direction = (0, i)
            make_move(lines, unvisited, current, direction)
            direction = (i, 0)
            make_move(lines, unvisited, current, direction)

    return []


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [[int(c) for c in line.strip()] for line in lines]

    dijkstra_aoc(lines)

if __name__ == '__main__':
    testing = True
    stage = 1
    start = time.time()
    task()
    print(time.time() - start)
    stage = 2
    start = time.time()
    task()
    print(time.time() - start)