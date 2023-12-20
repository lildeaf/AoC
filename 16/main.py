import time
import sys

sys.setrecursionlimit(10000)

def get_next_pos(current, direction):
    next_spot_y, next_spot_x = current[0], current[1]

    if direction == 0:#right
        next_spot_x += 1
    elif direction == 2: #left
        next_spot_x -= 1
    elif direction == 1: #up
        next_spot_y -= 1
    else: #down
        next_spot_y += 1
    return (next_spot_y, next_spot_x)

def check_oob(lines, pos):
    if pos[0] < 0 or pos[0] >= len(lines):
        return True
    if pos[1] < 0 or pos[1] >= len(lines[0]):
        return True

    return False

def gibIhm(lines, next, hits):
    if check_oob(lines, next):
        return

    trace(lines, next, hits)

def check(lines, pos, hits):
    for hit in hits:
        if hit[0] == pos[0] and hit[1] == pos[1] and \
                (lines[pos[0]][pos[1]] == '|' or lines[pos[0]][pos[1]] == '-'):
            return True

    return False

def trace(lines, current, hits):
    if check(lines, current, hits) or current in hits:
        return
    hits.append(current)

    direction = current[2]
    if lines[current[0]][current[1]] == '.':
        next_pos = get_next_pos(current, direction)
        next_cur = (next_pos[0], next_pos[1], direction)
        gibIhm(lines, next_cur, hits)
    elif lines[current[0]][current[1]] == '/':
        next_dir = (direction+1 if direction%2 == 0 else direction-1) % 4
        next_pos = get_next_pos(current, next_dir)
        next_cur = (next_pos[0], next_pos[1], next_dir)
        gibIhm(lines, next_cur, hits)
    elif lines[current[0]][current[1]] == '\\':
        next_dir = (direction - 1 if direction % 2 == 0 else direction + 1) % 4
        next_pos = get_next_pos(current, next_dir)
        next_cur = (next_pos[0], next_pos[1], next_dir)
        gibIhm(lines, next_cur, hits)
    elif lines[current[0]][current[1]] == '-':
        if direction%2 == 0:
            next_pos = get_next_pos(current, direction)
            next_cur = (next_pos[0], next_pos[1], direction)
            gibIhm(lines, next_cur, hits)
        else:
            next_dir = (direction - 1) % 4
            next_pos = get_next_pos(current, next_dir)
            next_cur = (next_pos[0], next_pos[1], next_dir)
            gibIhm(lines, next_cur, hits)
            next_dir = (direction + 1) % 4
            next_pos = get_next_pos(current, next_dir)
            next_cur = (next_pos[0], next_pos[1], next_dir)
            gibIhm(lines, next_cur, hits)
    else:
        if direction%2 == 1:
            next_pos = get_next_pos(current, direction)
            next_cur = (next_pos[0], next_pos[1], direction)
            gibIhm(lines, next_cur, hits)
        else:
            next_dir = (direction - 1) % 4
            next_pos = get_next_pos(current, next_dir)
            next_cur = (next_pos[0], next_pos[1], next_dir)
            gibIhm(lines, next_cur, hits)
            next_dir = (direction + 1) % 4
            next_pos = get_next_pos(current, next_dir)
            next_cur = (next_pos[0], next_pos[1], next_dir)
            gibIhm(lines, next_cur, hits)


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.split()[0] for line in lines]
    if stage == 1:
        hit = []
        current = (0, 0, 0)
        trace(lines, current, hit)
        hit = set([(i, j) for i, j, _ in hit])
        print(len(hit))
        return

    tiles = []
    for y in range(len(lines)):
        current = (y, 0, 0)
        hit = []
        trace(lines, current, hit)
        hit = set([(i, j) for i, j, _ in hit])
        tiles.append(len(hit))

        current = (y, len(lines[0])-1, 2)
        hit = []
        trace(lines, current, hit)
        hit = set([(i, j) for i, j, _ in hit])
        tiles.append(len(hit))

    for x in range(len(lines[0])):
        current = (0, x, 3)
        hit = []
        trace(lines, current, hit)
        hit = set([(i, j) for i, j, _ in hit])
        tiles.append(len(hit))

        current = (len(lines)-1, x, 1)
        hit = []
        trace(lines, current, hit)
        hit = set([(i, j) for i, j, _ in hit])
        tiles.append(len(hit))

    print("Stage 2:", max(tiles))


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