import time
import numpy as np
from heapq import heappop, heappush, heapify


def print_map(lines, poss, starty, endy, startx, endx, S, p=False):
    if not p:
        return
    for y in range(starty, endy):
        if y >= len(lines) or y < 0:
            continue
        for x in range(startx, endx):
            if x >= len(lines[y]) or x < 0:
                continue

            pos = (y, x)
            if S == pos:
                print('S', end='')
                continue
            if pos in poss:
                print('O', end='')
            else:
                print(lines[y][x], end='')
        print()


def check_corner(lines, pos):
    # left
    pos_y = pos[0]
    pos_x = pos[1] - 1
    left_block = False
    if pos_x < 0 or pos_x >= len(lines[0]) or lines[pos_y][pos_x] == '#':
        left_block = True
    # right
    pos_y = pos[0]
    pos_x = pos[1] + 1
    right_block = False
    if pos_x < 0 or pos_x >= len(lines[0]) or lines[pos_y][pos_x] == '#':
        right_block = True
    # top
    pos_y = pos[0] - 1
    pos_x = pos[1]
    top_block = False
    if pos_y < 0 or pos_y >= len(lines) or lines[pos_y][pos_x] == '#':
        top_block = True
    # bottom
    pos_y = pos[0] + 1
    pos_x = pos[1]
    bottom_block = False
    if pos_y < 0 or pos_y >= len(lines) or lines[pos_y][pos_x] == '#':
        bottom_block = True

    return left_block and right_block and top_block and bottom_block


def get_distances(lines, S, debug=False):
    d = [[np.inf for _ in range(len(lines[0]))] for _ in range(len(lines))]
    y = len(lines)
    x = len(lines[0])
    S_y, S_x = S

    d[S_y][S_x] = 0
    aft = [(np.sqrt((S_y - y) ** 2 + (S_x - x) ** 2), y, x) for y in range(len(lines)) for x in range(len(lines[0])) if
           lines[y][x] != '#']
    aft.remove((0, S_y, S_x))
    heapify(aft)

    while len(aft) > 0:
        aha, pos_y, pos_x = heappop(aft)  # aft.pop(0)
        up, bottom, left, right = np.inf, np.inf, np.inf, np.inf
        if 0 <= (pos_y + 1) < len(lines):
            bottom = d[pos_y + 1][pos_x] + 1
        if 0 <= (pos_y - 1) < len(lines):
            up = d[pos_y - 1][pos_x] + 1
        if 0 <= (pos_x + 1) < len(lines[0]):
            right = d[pos_y][pos_x + 1] + 1
        if 0 <= (pos_x - 1) < len(lines[0]):
            left = d[pos_y][pos_x - 1] + 1
        dist = min(d[pos_y][pos_x], up, bottom, left, right)
        if dist == np.inf and not check_corner(lines, (pos_y, pos_x)):
            heappush(aft, (aha + 1, pos_y, pos_x))  # aft.append((aha, pos_y, pos_x))
        d[pos_y][pos_x] = dist

    if debug:
        [print(di) for di in d]
        for i in range(0, y):
            for j in range(0, x):
                if lines[i][j] != '.':
                    print(lines[i][j], end='')
                    continue

                print("x" if d[i][j] == np.inf else d[i][j] % 10, end='')
            print()

    return d


def write_out(lines, d, steps):
    file = open("output.txt", 'w')
    new_lines = []

    for y in range(len(lines)):
        s = []
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                s.append('#')
                continue

            if d[y][x] < steps:
                s.append(str(d[y][x] % 10))
            else:
                s.append(lines[y][x])

        new_lines.append(''.join(s))

    file.write('\n'.join(new_lines))


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.split()[0] for line in lines]
    index = ''.join(lines).find('S')
    S_y = index // len(lines[0])
    S_x = index - (len(lines[0]) * S_y)
    S = (S_y, S_x)

    steps = 64
    debug = False
    distances = get_distances(lines, S, debug)

    step_count = 0
    count_even, count_odd = 0, 0
    count_ev_corner, count_od_corner = 0, 0
    for line in distances:
        for distance in line:
            if distance % 2 == 0 and distance < np.inf:
                count_even += 1
            if distance % 2 == 1 and distance < np.inf:
                count_odd += 1
            if distance % 2 == 1 and steps + 1 < distance < np.inf:
                count_od_corner += 1
            if distance % 2 == 0 and steps + 1 < distance < np.inf:
                count_ev_corner += 1
            if distance % 2 == 0 and distance <= steps:
                step_count += 1

    if stage == 1:
        write_out(lines, distances, steps)
        print("Stage 1:", step_count)
        return

    stage2_steps = 26501365
    n = stage2_steps // 131
    print(n)
    calc = (n + 1) ** 2 * count_odd + (n ** 2) * count_even - (n + 1) * count_od_corner + n * count_ev_corner
    print("Stage 2:", calc)


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
