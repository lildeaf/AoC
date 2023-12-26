import time


def checkExpansion(line):
    return all([x == '.' for x in line])


def getExpansions(expanded, start, end):
    count = 0
    for exp in expanded:
        if start < exp < end:
            count += 1

    return count


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [list(line.strip()) for line in lines]
    expansion_multiplier = 1 if stage == 1 else (1000000 - 1)

    expanded_y = [y for y in range(len(lines)) if checkExpansion(lines[y])]
    expanded_x = [x for x in range(len(lines[0])) if checkExpansion([line[x] for line in lines])]
    stars = [(y, x) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == '#']

    steps = []
    for i in range(len(stars)):
        i_y, i_x = stars[i]
        for j in range(i + 1, len(stars)):
            j_y, j_x = stars[j]
            start_x, end_x = (j_x, i_x) if j_x < i_x else (i_x, j_x)
            x_mult, y_mult = getExpansions(expanded_x, start_x, end_x), getExpansions(expanded_y, i_y, j_y)
            x_step, y_step = end_x - start_x, j_y - i_y
            steps.append(x_step + y_step + expansion_multiplier * (x_mult + y_mult))

    print("RESULT: ", sum(steps))


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