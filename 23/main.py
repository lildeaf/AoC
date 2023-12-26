import time

def get_longest(intersections, current, dest, visited, current_dist):
    if current == dest:
        return True, current_dist

    if current in visited:
        return False, 0

    neighbors = intersections[current]
    reached = False
    ways = [-1]
    curr_visited = visited.copy()
    curr_visited.add(current)
    for n in neighbors:
        point, dist = n
        tmp_reached, tmp_dist = get_longest(intersections, point, dest, curr_visited, current_dist+dist)
        if tmp_reached:
            dist = max(tmp_dist, dist)
            ways.append(dist)
            reached = True

    return reached, max(ways)

def check_slope(slope, direction):
    if direction == (0,1) and slope == '>':
        return True
    if direction == (0,-1) and slope == '<':
        return True
    if direction == (1,0) and slope == 'v':
        return True
    if direction == (-1,0) and slope == '^':
        return True

def get_directions(lines, pos, inv_dir):
    possible_directions = []
    for direction in [(0,1), (1,0), (-1,0), (0,-1)]:
        if direction == inv_dir:
            continue
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos[0] >= len(lines) or new_pos[0] < 0:
            continue
        if new_pos[1] >= len(lines[0]) or new_pos[1] < 0:
            continue

        if lines[new_pos[0]][new_pos[1]] == '#':
            continue

        if lines[new_pos[0]][new_pos[1]] == '.' or stage == 2 or check_slope(lines[new_pos[0]][new_pos[1]], direction):
            possible_directions.append(direction)

    return set(possible_directions)

def get_vertices(lines, pos, direction, visited):
    tmp_pos = pos
    tmp_direction = direction
    inv_dir = (-tmp_direction[0], -tmp_direction[1])
    distance = 1
    while len(possible := get_directions(lines, tmp_pos, inv_dir)) <= 1:
        distance += 1
        possible.discard(inv_dir)
        for p in possible:
            tmp_pos = (tmp_pos[0] + p[0], tmp_pos[1] + p[1])
            tmp_direction = p
            inv_dir = (-tmp_direction[0], -tmp_direction[1])
            break
        if tmp_pos == (len(lines) - 1, len(lines[0]) - 2):
            return distance, tmp_pos, None

    inv_dir = (-tmp_direction[0], -tmp_direction[1])
    possible.discard(inv_dir)

    if tmp_pos in visited:
        return distance, tmp_pos, None
    vertext_to_vert = {}
    vertex_distances = []
    visited.add(tmp_pos)
    for p in possible:
        next_pos = (tmp_pos[0] + p[0], tmp_pos[1] + p[1])
        next_dist, next_vert, next_vert_neigh = get_vertices(lines, next_pos, p, visited)
        vertex_distances.append([next_vert, next_dist])
        if next_vert_neigh == None:
            continue
        if stage == 2:
            next_vert_neigh[next_vert].append([tmp_pos, next_dist])

        vertext_to_vert.update(next_vert_neigh)

    vertext_to_vert[tmp_pos] = vertex_distances
    return distance, tmp_pos, vertext_to_vert

def print_map(lines, intersections):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (y,x) in intersections.keys():
                print('O', end='')
            else:
                print(lines[y][x], end='')
        print()


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.split()[0] for line in lines]

    start_point = (0, 1)
    destination = (len(lines) - 1, len(lines[0]) - 2)
    dist, tmp_pos, intersections = get_vertices(lines, (1,1), (1,0), {start_point})
    start_dict = {start_point : [[tmp_pos, dist]]}
    intersections.update(start_dict)

    result = get_longest(intersections, start_point, destination, set(), 0)
    print(f"Stage {stage}:", result[1])

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