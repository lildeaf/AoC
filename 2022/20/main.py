import time
import numpy as np


# implementation for stage 1 in plain python
def one(lines):
    coords = []

    for line in lines:
        coords.append((int(line.strip()), 0))

    print(coords)
    i = 0
    cnt = 0
    while cnt < len(coords):
        val, fin = coords[i]
        if fin == 1:
            i += 1
            continue

        # print("BEF", coords, i)
        coords.pop(i)
        new_i = (i + val) % (len(coords))
        coords.insert(new_i, (val, 1))
        # print("AFT", coords, new_i, new_i % (len(coords)+1))
        # print(cnt)
        cnt += 1

        if new_i <= i:
            i += 1

    zero = coords.index((0, 1))
    print(zero)
    nums = []
    for i in range(1, 4):
        index = (i * 1000) + zero
        index = index % len(coords)

        print(i * 1000, index, coords[index][0])
        nums.append(coords[index][0])

    print(sum(nums))


# implementation for stage 2(and stage 1) in plain python
def two(coords, indices):
    for i, index in enumerate(indices):
        val = coords.pop(index)
        new_i = (index + val) % (len(coords))
        coords.insert(new_i, val)
        for j, old in enumerate(indices):
            if old == index:
                indices[j] = new_i
                continue

            if new_i <= old < index:
                indices[j] += 1

            if index < old <= new_i:
                indices[j] -= 1

        #print(i, coords, indices)

    return coords, indices


# implementation for stage 2(and stage 1) with numpy
def nptwo(coords, indices):
    i = -1
    while (i := i + 1) < len(indices):
        index = indices[i]
        val = coords.pop(index)
        new_i = (index + val) % (len(coords))
        coords.insert(new_i, val)

        indices = np.where((new_i <= indices) & (indices < index), indices + 1, indices)
        indices = np.where((new_i >= indices) & (indices > index), indices - 1, indices)
        indices[i] = new_i

    return coords, indices



def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    coords = []

    for line in lines:
        coords.append(int(line.strip()) * (1 if stage == 1 else 811589153))

    indices = np.array([i for i in range(len(coords))])
    for i in range(1 if stage == 1 else 10):
        #coords, indices = nptwo(coords, indices)
        coords, indices = two(coords, indices)

        #print(i, coords)

    zero = coords.index(0)
    nums = []
    for i in range(1, 4):
        index = (i * 1000) + zero
        index = index % len(coords)
        nums.append(coords[index])

    print(sum(nums))

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
