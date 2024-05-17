import time
from heapq import heappop, heappush, heapify

def print_map(states, i, y_max, x_max):
    slice = states[i]

    print("MINUTE", i)
    print('#' * (x_max+1))
    for y in range(1, y_max+1):
        row = slice.get(y, {})
        print('#', end='')
        for x in range(1, x_max+1):
            pos = row.get(x, None)
            if pos is None:
                print('.', end='')
            else:
                print(list(pos)[0] if len(pos) == 1 else len(pos), end='')
        print('#')
    print('#' * (x_max + 1))

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]

    x_min = 1
    y_min = 1
    x_max = 6 if testing else 120
    y_max = 4 if testing else 25

    max_states = 12 if testing else 600
    states = [{} for _ in range(max_states)]

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '<' or c == '>':
                for i in range(max_states):
                    slice = states[i]
                    lr = slice.get(y, {})
                    correct_x = (x + (-i if c == '<' else i)) - 1
                    correct_x = (correct_x % x_max) + 1
                    position = lr.get(correct_x, set())
                    position.add(c)

                    lr[correct_x] = position
                    slice[y] = lr
                    states[i] = slice

            if c == '^' or c == 'v':
                for i in range(max_states):
                    slice = states[i]
                    correct_y = (y + (-i if c == '^' else i)) - 1
                    correct_y = (correct_y % y_max) + 1
                    lr = slice.get(correct_y, {})
                    position = lr.get(x, set())
                    position.add(c)

                    lr[x] = position
                    slice[correct_y] = lr
                    states[i] = slice

    #for i in range(max_states):
    #    print_map(states, i, y_max, x_max)
    #print(states[0])

    pos_queue = [(0, (1, 0))] #initial position (time, (x, y))
    destinations = [(x_max, y_max+1)] if stage == 1 else [(x_max, y_max+1), (x_min, 0) ,(x_max, y_max+1)]
    count = 0
    heapify(pos_queue)

    visited = set()
    while True:
        timestamp, pos = heappop(pos_queue)

        if (timestamp % max_states, pos) in visited:
            continue

        visited.add((timestamp % max_states, pos))
        if pos == destinations[count]:
            if count == (0 if stage == 1 else 2):
                print(timestamp)
                break
            count += 1
            visited.clear()
            pos_queue.clear()

        x, y = pos
        next_timestamp = timestamp + 1
        next_state = states[next_timestamp % max_states]

        row = next_state.get(y, {})
        for step in range(-1, 2, 2):
            if (new_x := x+step) not in row.keys():
                if x_min <= new_x <= x_max and y_min <= y <= y_max:
                    heappush(pos_queue, (next_timestamp, (new_x, y))) # STEP TO LEFT OR RIGHT

            new_y = y+step
            tmp_row = next_state.get(new_y, {})
            if x not in tmp_row.keys():
                if y_min <= new_y <= y_max and x_min <= x <= x_max:
                    heappush(pos_queue, (next_timestamp, (x, new_y))) # STEP TO UP OR DOWN

        if x == x_max and y == y_max:
            heappush(pos_queue, (next_timestamp, (x_max, y_max+1)))

        if stage == 2 and x == x_min and y == y_min:
            heappush(pos_queue, (next_timestamp, (x_min, y_min-1)))

        if x not in row.keys():
            heappush(pos_queue, (next_timestamp, (x, y))) #WAITING


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
