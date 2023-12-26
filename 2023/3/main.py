import time
import re


def checkIfPart(c):
    return (not c.isdigit() and not c == '.' and not c == '\n') if stage == 1 else (c == '*')


def getNumbers(lines, part):
    (x, y) = part
    pattern = re.compile("\d+")

    numbers = ([match for match in pattern.finditer(lines[y])])
    if y - 1 >= 0:
        numbers.extend([match for match in pattern.finditer(lines[y - 1])])
    if y < len(lines):
        numbers.extend([match for match in pattern.finditer(lines[y + 1])])

    adj_numbers = [int(match.group()) for match in numbers if not (match.start() > x + 1 or match.end() < x)]
    result = sum(adj_numbers)  # stage 1
    if stage == 2:
        result = 0 if not len(adj_numbers) == 2 else adj_numbers[0] * adj_numbers[1]

    return result


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    parts = [(x, y) for y in range(len(lines)) for x in range(len(lines[y])) if checkIfPart(lines[y][x])]
    nums = [getNumbers(lines, part) for part in parts]

    num_sums = sum(nums)
    print(f"Result {stage}: {num_sums}")


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
