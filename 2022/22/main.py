import time
import re


def steps(curr, map, k, direc, count):
    positions = map[k]
    length = len(positions)

    while (count := count - 1) >= 0:
        idx = positions.index(curr) + direc
        tmp = positions[idx % length]
        if not tmp[1]:
            break

        curr = tmp

    return curr


def stage1(input_lines):
    directions = ['r', 'b', 'l', 't']
    y2x, x2y = dict(), dict()

    for y, line in enumerate(input_lines[:-2]):
        for x, c in enumerate(line.strip('\n')):
            if c == '.' or c == '#':
                tmp = y2x.get(y, [])
                tmp.append((x, c == '.'))
                y2x[y] = tmp

                tmp = x2y.get(x, [])
                tmp.append((y, c == '.'))
                x2y[x] = tmp

    instructions = [x.group() for x in re.finditer('(\d+)|(R|L)', input_lines[-1].strip())]

    print(instructions)
    # print(y2x)
    start = y2x[0][0]
    direction = 'r'
    # if leftmost element is rock, only works if at least one element is not a rock
    while not start[1]:
        idx = y2x[0].index(start)
        start = y2x[0][idx + 1]

    pos = start
    k = 0
    for i, instr in enumerate(instructions):
        if i % 2 == 1:
            n = directions.index(direction) + (1 if instr == 'R' else -1)
            direction = directions[n % len(directions)]
            tmp_k = pos[0]
            pos = (k, True)
            k = tmp_k
            # change dir
        else:
            k_row = direction == 'r' or direction == 'l'
            map_param = x2y if direction == 't' or direction == 'b' else y2x
            dir_param = 1 if direction == 'r' or direction == 'b' else -1
            # print("BEF", (k, pos[0]) if k_row else (pos[0], k))
            pos = steps(pos, map_param, k, dir_param, int(instr))
            # print("AFT", (k, pos[0]) if k_row else (pos[0], k))
            # print()
            # print(pos, k, direction)
            # step

    k_row = direction == 'r' or direction == 'l'
    result = (k + 1) * (1000 if k_row else 4) + (pos[0] + 1) * (4 if k_row else 1000) + directions.index(direction)
    print(result)


def left(faces):
    faces[0]["l"] = (4, "r")
    faces[1]["l"] = (0, "l")
    faces[2]["l"] = (4, "d")
    faces[3]["l"] = (4, "l")
    faces[4]["l"] = (0, "r")
    faces[5]["l"] = (0, "d")


def right(faces):
    faces[0]["r"] = (1, "r")
    faces[1]["r"] = (3, "l")
    faces[2]["r"] = (1, "t")
    faces[3]["r"] = (1, "l")
    faces[4]["r"] = (3, "r")
    faces[5]["r"] = (3, "t")


def top(faces):
    faces[0]["t"] = (5, "r")
    faces[1]["t"] = (5, "t")
    faces[2]["t"] = (0, "t")
    faces[3]["t"] = (2, "t")
    faces[4]["t"] = (2, "r")
    faces[5]["t"] = (4, "t")


def down(faces):
    faces[0]["d"] = (2, "d")
    faces[1]["d"] = (2, "l")
    faces[2]["d"] = (3, "d")
    faces[3]["d"] = (5, "l")
    faces[4]["d"] = (5, "d")
    faces[5]["d"] = (1, "d")


def step_cube(faces, direction, current_face, pos):
    directions = ['r', 'd', 'l', 't']
    face = faces[current_face]
    next_vals = face[direction]
    next_face = faces[next_vals[0]]
    next_dir = next_vals[1]
    next_pos = pos
    layout = next_face["layout"]

    same = abs(directions.index(direction) - directions.index(next_dir))
    if same == 0:  # same direction
        if (right_dir := next_dir == 'r') or next_dir == 'l':
            tmp_pos = (0 if right_dir else 49, pos[1])
        else:
            tmp_pos = (pos[0], 0 if next_dir == 'd' else 49)

        if layout[tmp_pos[1]][tmp_pos[0]] != '#':
            return next_vals[0], tmp_pos, next_dir
    elif same == 2:  # 180 turn
        if (right_dir := next_dir == 'r') or next_dir == 'l':
            tmp_pos = (0 if right_dir else 49, 49 - pos[1])
        else:
            tmp_pos = (49 - pos[0], 0 if next_dir == 'd' else 49)

        if layout[tmp_pos[1]][tmp_pos[0]] != '#':
            return next_vals[0], tmp_pos, next_dir
        pass
    else:
        if (right_dir := next_dir == 'r') or next_dir == 'l':
            tmp_pos = (0 if right_dir else 49, pos[0])
        else:
            tmp_pos = (pos[1], 0 if next_dir == 'd' else 49)

        if layout[tmp_pos[1]][tmp_pos[0]] != '#':
            return next_vals[0], tmp_pos, next_dir

    return current_face, pos, direction


def stage2(input_lines):

    # face: layout:[],
    #      for each side: [faceid, new_dir, flip?]
    #lines = [line.strip() for line in lines]

    length = 50
    faces = {i: {"layout": [], "left": 0, "right": 0, "top": 0, "down": 0} for i in range(6)}
    start_x = [50, 100, 50, 50, 0, 0]
    start_y = [0, 0, 50, 100, 100, 150]
    for i in range(6):
        face = faces[i]
        for y in range(start_y[i], start_y[i] + length):
            # print(lines[y][start_x[i]:start_x[i]+50])
            face["layout"].append(input_lines[y][start_x[i]:start_x[i] + length])

    left(faces)
    right(faces)
    top(faces)
    down(faces)

    directions = ['r', 'd', 'l', 't']
    current_face = 0
    pos = (0, 0)
    direction = 'r'
    instructions = [x.group() for x in re.finditer('(\d+)|(R|L)', input_lines[-1].strip())]

    print(instructions)
    for i, instr in enumerate(instructions):
        if i % 2 == 1:
            n = directions.index(direction) + (1 if instr == 'R' else -1)
            direction = directions[n % len(directions)]
        else:
            for _ in range(int(instr)):
                if (direction == 't' and pos[1] == 0) or \
                        (direction == 'd' and pos[1] == 49) or \
                        (direction == 'r' and pos[0] == 49) or \
                        (direction == 'l' and pos[0] == 0):
                    current_face, pos, direction = step_cube(faces, direction, current_face, pos)  # LOOP AROUND CUBE
                else:
                    # NORMAL STEP
                    layout = faces[current_face]["layout"]
                    if direction == 'r' or direction == 'l':
                        if layout[pos[1]][pos[0] + (change := 1 if direction == 'r' else -1)] != '#':
                            pos = (pos[0] + change, pos[1])
                    else:
                        if layout[pos[1] + (change := 1 if direction == 'd' else -1)][pos[0]] != '#':
                            pos = (pos[0], pos[1] + change)

    last_x = start_x[current_face] + pos[0] + 1
    last_y = start_y[current_face] + pos[1] + 1
    result = last_y * 1000 + last_x * 4 + directions.index(direction)
    print(result)


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    if stage == 1:
        stage1(lines)
    else:
        stage2(lines)


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
