import time

def update_head(pos, direction):
    if direction == 1:
        return (pos[0], pos[1]+1)
    if direction == -1:
        return (pos[0], pos[1]-1)
    if direction == 2:
        return (pos[0]-1, pos[1])
    if direction == -2:
        return (pos[0]+1, pos[1])

def check_distance(head, tail):
    y = (head[0] - tail[0])**2
    x = (head[1] - tail[1])**2

    return x+y

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    positions = {}
    positions[(0,0)] = 1

    directions = {'R': 1, 'L': -1, 'U': 2, 'D': -2}

    knot_positions = [(0, 0) for _ in range(2 if stage == 1 else 10)]

    for line in lines:
        direction, steps = line.split()
        for _ in range(int(steps)):
            relative = False
            new_pos = knot_positions.copy()
            new_pos[0] = update_head(knot_positions[0], directions[direction])
            for i in range(1, len(knot_positions)):
                if check_distance(new_pos[i-1], knot_positions[i]) > 2:
                    prev_knot = new_pos[i-1]
                    current_knot = knot_positions[i]
                    y_diff = prev_knot[0] - knot_positions[i-1][0]
                    x_diff = prev_knot[1] - knot_positions[i-1][1]
                    if relative:
                        y_new_diff = prev_knot[0] - current_knot[0]
                        x_new_diff = prev_knot[1] - current_knot[1]
                        if x_new_diff != 0 and y_new_diff != 0:
                            new_pos[i] = (current_knot[0] + y_diff, current_knot[1] + x_diff)
                        else:
                            relative = False
                            new_pos[i] = (prev_knot[0] - y_new_diff//2, prev_knot[1] - x_new_diff//2)
                        continue

                    new_pos[i] = (prev_knot[0] - y_diff, prev_knot[1] - x_diff)
                    y_diff = new_pos[i][0] - current_knot[0]
                    x_diff = new_pos[i][1] - current_knot[1]
                    relative = (x_diff != 0 and y_diff != 0)
                else:
                    break
            knot_positions = new_pos
            positions[knot_positions[-1]] = 1

    print(sum(positions.values()))


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
