import time
import re


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    result = []
    for line in lines:
        game_id = int(re.search("\d+", line).group())
        cube_sets = line.split(':')[1]
        red_cubes = [int(n) for n in re.findall("(\d+) red", cube_sets)]
        green_cubes = [int(n) for n in re.findall("(\d+) green", cube_sets)]
        blue_cubes = [int(n) for n in re.findall("(\d+) blue", cube_sets)]

        red_possibles = [cube <= 12 for cube in red_cubes]
        green_possibles = [cube <= 13 for cube in green_cubes]
        blue_possibles = [cube <= 14 for cube in blue_cubes]

        if stage == 1 and all(red_possibles + green_possibles + blue_possibles):
            result.append(game_id)

        if stage == 2:
            result.append(max(red_cubes) * max(green_cubes) * max(blue_cubes))

    print(sum(result))


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
