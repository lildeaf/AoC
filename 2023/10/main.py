import time

# N = 0, S = 1, E= 2, W=3
possible_pipes = {
    0: ['|', '7', 'F'],
    1: ['-', 'J', '7'],
    2: ['|', 'L', 'J'],
    3: ['-', 'F', 'L']
}

def get_start_positions(lines, x, y):
    new_x = []
    new_y = []
    new_d = []

    if lines[y - 1][x] in possible_pipes[(d := 0)]:
        new_d.append(d)
        new_x.append(x)
        new_y.append(y - 1)
    if lines[y][x + 1] in possible_pipes[(d := 1)]:
        new_d.append(d)
        new_x.append(x + 1)
        new_y.append(y)
    if lines[y + 1][x] in possible_pipes[(d := 2)]:
        new_d.append(d)
        new_x.append(x)
        new_y.append(y + 1)
    if lines[y][x - 1] in possible_pipes[(d := 3)]:
        new_d.append(d)
        new_x.append(x - 1)
        new_y.append(y)

    return new_x, new_y, new_d

def get_direction(lines, x, y, direction):
    pipe = lines[y][x]
    index = possible_pipes[direction].index(pipe)
    if index > 0:
        return direction + (-1 if index == 1 else 1)

    return direction

def get_next_pos(x, y, direction):
    if direction == 0:
        return x, y-1
    elif direction == 1:
        return x+1, y
    elif direction == 2:
        return x, y+1
    else:
        return x-1, y

def change_S(directions):
    if 0 in directions:
        other = [x for x in directions if x != 0][0]
        return possible_pipes[0][other] if other == 1 else possible_pipes[0][(other - 2) * 2]
    elif 2 in directions:
        other = [x for x in directions if x != 2][0]
        return possible_pipes[0][(other + 1) % 3]
    else:
        return '-'

def task():
    filename = 'input.txt'
    if testing:
        filename = 'example.txt' if stage == 1 else 'example2.txt'
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    index = ''.join(lines).find('S')
    S_y = index // len(lines[0])
    S_x = index - (len(lines[0]) * S_y)
    min_x, min_y = S_x, S_y
    max_x, max_y = S_x, S_y

    lines = [[c for c in line] for line in lines]

    pos_x, pos_y, d = get_start_positions(lines, S_x, S_y)
    n_x1, n_y1, d1 = pos_x[0], pos_y[0], d[0]
    n_x2, n_y2, d2 = pos_x[1], pos_y[1], d[1]
    lines[S_y][S_x] = change_S(d)

    # setup for stage 2 to apply even-odd-algorithm
    max_x, max_y = max(max_x, n_x1, n_x2), max(max_y, n_y1, n_y2)
    min_x, min_y = min(min_x, n_x1, n_x2), min(min_y, n_y1, n_y2)
    # indices of loop saved as dictionary
    loop = {y: [] for y in range(len(lines))}
    loop[S_y] = loop[S_y] + [S_x]
    loop[n_y1] = loop[n_y1] + [n_x1]
    loop[n_y2] = loop[n_y2] + [n_x2]

    count = 1
    while not (n_x1 == n_x2 and n_y1 == n_y2):
        tmp_d1 = get_direction(lines, n_x1, n_y1, d1) % 4
        tmp_d2 = get_direction(lines, n_x2, n_y2, d2) % 4
        d1, d2 = tmp_d1, tmp_d2

        n_x1, n_y1 = get_next_pos(n_x1, n_y1, d1)
        n_x2, n_y2 = get_next_pos(n_x2, n_y2, d2)

        #getting bounding box of loop and setting loop indices
        max_x, max_y = max(max_x, n_x1, n_x2), max(max_y, n_y1, n_y2)
        min_x, min_y = min(min_x, n_x1, n_x2), min(min_y, n_y1, n_y2)
        loop[n_y1] = loop[n_y1] + [n_x1]
        loop[n_y2] = loop[n_y2] + [n_x2]

        count += 1

    if stage == 1:
        print("Stage 1 result:", count)
        return

    inside = 0
    last_hit = ''
    for y in range(min_y+1, max_y):
        in_poly = 0
        for x in range(max(0, min_x-1), max_x+1):
            tile = lines[y][x]
            if x in loop[y] and tile in ['|', 'L', 'F']:
                last_hit = tile
                in_poly += 1
                continue
            if x in loop[y] and tile == 'J' and last_hit == 'L':
                last_hit = tile
                in_poly += 1
                continue
            if x in loop[y] and tile == '7' and last_hit == 'F':
                last_hit = tile
                in_poly += 1
                continue

            if not (x in loop[y]) and in_poly%2 == 1:
                lines[y][x] = 'I'
                inside += 1

    #print(''.join([''.join(line) for line in lines]))
    print("Stage 2 result:", inside)

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