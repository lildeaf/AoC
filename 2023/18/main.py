import time
import numpy as np

direction_mapping = {
    'U': np.array([-1, 0]),
    'D': np.array([1, 0]),
    'L': np.array([0, -1]),
    'R': np.array([0, 1])
}

def get_next(start, direction, num):
    return start + direction_mapping[direction]*num

#Draw polygon for stage 1 in terminal
def draw_poly_1(min_x, max_x, min_y, max_y, vertices, edges, directions):
    normal = np.abs(np.array([min_y, min_x]))
    vertices = [vertex + normal for vertex in vertices]
    width = (max_x + 1 - min_x)
    height = (max_y + 1 - min_y)
    field = [['.' for _ in range(width)] for _ in range(height)]

    for edge in edges:
        start = vertices[edge]
        direction, num, color = directions[edge]
        for i in range(num + 1):
            curr = start + direction_mapping[direction] * i
            field[curr[0]][curr[1]] = '#'

    [print(''.join(row)) for row in field]

def get_direction(num):
    dir_dict = {
        0: 'R',
        1: 'D',
        2: 'L',
        3: 'U'
    }

    return dir_dict[num]

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    directions = [(line.split()[0], int(line.split()[1]), line.split()[2][2:-1]) for line in lines]
    vertices = [[0, 0]]
    edges = []
    max_y, max_x = 0, 0
    min_y, min_x = 0, 0

    calcs, bs = [], []
    for i, direct in enumerate(directions):
        direction = direct[0] if stage == 1 else get_direction(int(direct[2][-1]))
        distance = direct[1] if stage == 1 else int(direct[2][:-1], 16)
        prev_vertex = vertices[-1]
        next_vertex = get_next(prev_vertex, direction, distance)

        max_y, max_x = max(next_vertex[0], max_y), max(next_vertex[1], max_x)
        min_y, min_x = min(next_vertex[0], min_y), min(next_vertex[1], min_x)

        bs.append(distance)
        tmp = np.multiply(prev_vertex, next_vertex[::-1], dtype='int64')
        calcs.append(tmp[0] - tmp[1])

        edges.append(i)
        vertices.append(next_vertex)

    if stage == 1 and testing:
        draw_poly_1(min_x, max_x, min_y, max_y, vertices, edges, directions)

    b = np.sum(bs, dtype='int64')
    area = np.abs(np.sum(calcs, dtype='int64') // 2)
    # Pick's Theorem
    inner = area + 1 - (b//2)
    print(inner + b)


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