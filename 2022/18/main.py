import time

def check_slice(slices, key, new_val):
    if (sl := slices.get(key, None)) is not None:
        sl.append(new_val)
        pass
    else:
        new_slice = [new_val]
        slices[key] = new_slice


def count_sclice(slices):
    counter = 0
    for key in slices:
        s = sorted(slices[key])
        if len(s) == 1:
            counter += 2
            continue

        for i in range(1,len(s)-1):
            coord = s[i]
            if s[i-1] != coord - 1:
                counter += 1
            if s[i+1] != coord + 1:
                counter += 1

        counter += 2 if s[0] + 1 != s[1] else 1
        counter += 2 if s[-1] - 1 != s[-2] else 1

    return counter


def get_neighbor(cube):
    neighborhood = []
    for i in range(-1, 2, 2):
        neighborhood.append((cube[0] + i, cube[1], cube[2]))
        neighborhood.append((cube[0], cube[1] + i, cube[2]))
        neighborhood.append((cube[0], cube[1], cube[2] + i))

    return neighborhood


def grid_step(cubes, start, end):
    queue = set()
    visited = set()
    queue.add(start)
    counter = 0

    while len(queue) > 0:
        current = queue.pop()

        if current in visited:
            continue

        visited.add(current)

        for n in get_neighbor(current):
            if n in cubes:
                counter += 1
                continue

            if (start[0] <= n[0] <= end[0]) and (start[1] <= n[1] <= end[1]) and (start[2] <= n[2] <= end[2]):
                queue.add(n)

    print(counter)


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    cubes = set()
    max_x, max_y, max_z = 0, 0, 0
    min_x, min_y, min_z = 0, 0, 0

    xy_sclice = {}
    yz_sclice = {}
    zx_sclice = {}

    for line in lines:
        cube = tuple(int(coord) for coord in line.strip().split(','))
        x,y,z = cube
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)

        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        check_slice(xy_sclice, (x, y), z)
        check_slice(yz_sclice, (y, z), x)
        check_slice(zx_sclice, (z, x), y)
        cubes.add(cube)

    start = (min_x - 1, min_y - 1, min_z - 1)
    end = (max_x + 1, max_y+ 1, max_z+ 1)

    xy_count = count_sclice(xy_sclice)
    yz_count = count_sclice(yz_sclice)
    zx_count = count_sclice(zx_sclice)
    print(xy_count + yz_count + zx_count)
    if stage == 2:
        grid_step(cubes, start, end)


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
