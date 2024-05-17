import time


def update_next(next_elves, new_pos, prev):
    nexts = next_elves.get(new_pos, [])
    nexts.append(prev)
    next_elves[new_pos] = nexts


def print_map(elves, round):
    (min_x, min_y), (max_x, max_y) = smallest_rect(elves)

    x_diff = max_x - min_x
    y_diff = max_y - min_y

    print("AFTER ROUND", round)
    for y in range(y_diff+1):
        for x in range(x_diff+1):
            pos = (x+min_x, y+min_y)
            if pos in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()


def check_surrounding(pos, elves):
    x, y = pos

    surrounding = set()
    for y_diff in range(-1, 2, 1):
        for x_diff in range(-1, 2, 1):
            check_pos = (x+x_diff, y+y_diff)
            if check_pos in elves:
                if y_diff == -1:
                    surrounding.add('N')
                if y_diff == 1:
                    surrounding.add('S')
                if x_diff == -1:
                    surrounding.add('W')
                if x_diff == 1:
                    surrounding.add('E')

                #num = (y_diff + 1) * 3 + (x_diff + 1)
                #surrounding |= (1 << num)

    return surrounding


def smallest_rect(elves):
    min_x, min_y = 99999999999999, 99999999999999
    max_x, max_y = -99999999999999, -99999999999999

    for e in elves:
        x, y = e
        min_x = min(min_x, x)
        max_x = max(max_x, x)

        min_y = min(min_y, y)
        max_y = max(max_y, y)

    return (min_x, min_y), (max_x, max_y)


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]

    elves = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.add((x,y))

    sides = ['N', 'S', 'W', 'E']
    next_elves = {}
    i = 0
    while (i < 10 if stage == 1 else True):
        no_move = 0
        #print_map(elves, i)
        next_elves.clear()

        for k in elves:
            x, y = k
            surrounding = check_surrounding(k, elves)
            if len(surrounding) == 0:
                update_next(next_elves, k, k)
                no_move += 1
                continue
            for d in sides:
                if d in surrounding:
                    continue
                if d == 'N':
                    new_pos = (x, y - 1)
                    update_next(next_elves, new_pos, k)
                    break
                elif d == 'S':
                    new_pos = (x, y + 1)
                    update_next(next_elves, new_pos, k)
                    break
                elif d == 'W':
                    new_pos = (x - 1, y)
                    update_next(next_elves, new_pos, k)
                    break
                elif d == 'E':
                    new_pos = (x + 1, y)
                    update_next(next_elves, new_pos, k)
                    break
            else:
                update_next(next_elves, k, k)

        if no_move == len(elves):
            print("NO MOVE AT", i+1)
            break
        sides.append(sides.pop(0))

        elves.clear()
        for k in next_elves:
            tmp = next_elves[k]
            if len(tmp) == 1:
                elves.add(k)
            else:
                for e in tmp:
                    elves.add(e)

        i += 1

    #print_map(elves, i)
    if stage == 1:
        (min_x, min_y), (max_x, max_y) = smallest_rect(elves)

        dim_x = (max_x - min_x) + 1
        dim_y = (max_y - min_y) + 1
        print(dim_x * dim_y - len(elves))


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
