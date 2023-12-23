import time
from functools import cmp_to_key
import numpy as np


def get_blocks(start, end):
    blocks = []
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for z in range(start[2], end[2] + 1):
                blocks.append([x, y, z])

    return np.array(blocks)


def compare(item1, item2):
    z1 = item1[1][0][2]
    z2 = item2[1][0][2]

    if z1 < z2:
        return -1

    if z1 > z2:
        return 1

    return 0


def rm(current, dis, above, under):
    if under[current].issubset(dis):
        dis.add(current)
    else:
        return 0

    counter = 0
    for brick_above in above[current]:
        counter += rm(brick_above, dis, above, under)

    return counter + 1


def write_to_file(grid):
    file = open("output.txt", 'w')
    out_lines = []
    max_x, max_y, max_z = grid.shape
    for x in range(max_x):
        for y in range(max_y):
            out_lines.append(' '.join([str(int(c)).zfill(4) for c in grid[x, y, :]]))

    file.write('\n'.join(out_lines))


def build_grid(bricks, max_x, max_y, max_z):
    grid = np.zeros((max_x + 1, max_y + 1, max_z + 1))  # 3 dimensional grid to set positions of bricks
    lowest_z = np.zeros((max_x + 1, max_y + 1))  # smallest z where block could fall down to
    above = {brick[0]: set() for brick in bricks}  # blocks above brick_id(key)
    under = {brick[0]: set() for brick in bricks}  # blocks under brick_id(key)

    for i, brick in enumerate(bricks):
        brick_id, blocks = brick
        smallest_diff = max_z
        # get highest z where brick can fall to
        for block in blocks:
            pos_x, pos_y, pos_z = block
            diff = pos_z - lowest_z[pos_x, pos_y]
            smallest_diff = min(diff - 1, smallest_diff)

        blocks[:, 2] = blocks[:, 2] - smallest_diff
        bricks_under = set()
        # adjusting lowest_z array and building above/under sets
        for block in blocks:
            pos_x, pos_y, pos_z = block
            if (block_under := grid[pos_x, pos_y, pos_z - 1]) != 0:
                bricks_under.add(block_under)
                above[block_under].add(brick_id)

            lowest_z[pos_x, pos_y] = pos_z
        under[brick_id] = bricks_under
        #bricks[i] = (brick_id, blocks)
        for block in blocks:
            grid[tuple(block)] = brick_id

    return grid, under, above


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    # (id, [blocks])
    bricks = []  # all bricks
    max_x, max_y, max_z = 0, 0, 0
    ids = 1
    # print("READ LINES")
    for line in lines:
        coords = line.strip().split('~')
        start = [int(n) for n in coords[0].split(',')]
        end = [int(n) for n in coords[1].split(',')]

        blocks = get_blocks(start, end)
        max_x = max(np.max(blocks[:, 0]), max_x)
        max_y = max(np.max(blocks[:, 1]), max_y)
        max_z = max(np.max(blocks[:, 2]), max_z)

        brick = (ids, blocks)
        bricks.append(brick)
        ids += 1

    bricks = sorted(bricks, key=cmp_to_key(compare))
    grid, under, above = build_grid(bricks, max_x, max_y, max_z)
    print(under)
    print(above)

    fall = {}
    for brick in bricks:
        brick_id = brick[0]
        supporting = above[brick_id]

        fall_set = {brick_id}
        counter = 0
        for brick_above in supporting:
            counter += rm(brick_above, fall_set, above, under)

        fall[brick_id] = counter

    if stage == 1:
        print("Stage 1:", list(fall.values()).count(0))
        return

    print("Stage 2:", sum(list(fall.values())))
    write_to_file(grid)


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
