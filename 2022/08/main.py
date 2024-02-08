import time

#could merge top/bottom and right/left and then use with caches(dynammic programming)
def check_top(x, y, lines, height):
    ret_value = 0 if stage == 1 else 1
    if lines[y][x] >= height:
        return ret_value

    if y == 0:
        return 1

    return check_top(x, y - 1, lines, height) + ret_value

def check_bottom(x, y, lines, height):
    ret_value = 0 if stage == 1 else 1
    if lines[y][x] >= height:
        return ret_value

    if y == len(lines)-1:
        return 1

    return check_bottom(x, y + 1, lines, height) + ret_value

def check_right(x, y, lines, height):
    ret_value = 0 if stage == 1 else 1
    if lines[y][x] >= height:
        return ret_value

    if x == len(lines[y])-1:
        return 1

    return check_right(x + 1, y, lines, height) + ret_value

def check_left(x, y, lines, height):
    ret_value = 0 if stage == 1 else 1
    if lines[y][x] >= height:
        return ret_value

    if x == 0:
        return 1

    return check_left(x - 1, y, lines, height) + ret_value


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = [line.strip() for line in input_file.readlines()]
    lines = [[int(c) for c in line] for line in lines]

    visibles = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if y == 0 or y == len(lines) - 1 or x == 0 or x == len(lines) - 1:
                visibles.append(1)
                continue

            top = check_top(x, y - 1, lines, lines[y][x])
            bottom = check_bottom(x, y + 1, lines, lines[y][x])
            left = check_left(x - 1, y, lines, lines[y][x])
            right = check_right(x + 1, y, lines, lines[y][x])
            if stage == 2:
                visibles.append(top * bottom * left * right)

            if stage == 1 and (top or bottom or left or right):
                visibles.append(1)

    print(sum(visibles) if stage == 1 else max(visibles))


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
