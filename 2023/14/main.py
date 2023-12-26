import time


def tilt(lines, reverse):
    new_lines = []
    for line_i, line in enumerate(lines):
        tmp_line = line[::-1] if reverse else line

        lowest = 0
        for i, c in enumerate(tmp_line):
            index = i
            if c == '#':
                lowest = index + 1
            if c == 'O':
                if lowest != index:
                    tmp_line[lowest] = 'O'
                    tmp_line[index] = '.'

                lowest += 1

        new_lines.append(tmp_line[::-1] if reverse else tmp_line)

    return new_lines


def spin_cycle(lines):
    # NORTH ROTATION
    lines = list(map(list, zip(*lines)))
    lines = tilt(lines, False)

    # WEST ROTATION
    lines = list(map(list, zip(*lines)))
    lines = tilt(lines, False)

    # SOUTH ROTATION
    lines = list(map(list, zip(*lines)))
    lines = tilt(lines, True)

    # EAST ROTATION
    lines = list(map(list, zip(*lines)))
    lines = tilt(lines, True)

    return [''.join(line) for line in lines]


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    cache = {tuple(lines): -1}
    cycles = 1000000000

    for i in range(1, cycles+1):
        if stage == 1:
            break
        lines = spin_cycle(lines)
        if tuple(lines) in cache:
            p_start = cache[tuple(lines)]
            diff = i - p_start
            for k, v in cache.items():
                if (v - p_start) == (cycles - p_start) % diff:
                    lines = list(k)
                    break
            break
        else:
            cache[tuple(lines)] = i

    lines = list(map(list, zip(*lines)))
    result = []
    for line in lines:
        lowest = 0
        rocks = []
        for i, c in enumerate(line):
            if c == '#':
                lowest = i + 1
            if c == 'O':
                rocks.append(len(line) - (lowest if stage == 1 else i))
                lowest += 1

        result.extend(rocks)

    print(f"Stage {stage}:", sum(result))


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
