import time

rocks = {
    0: [(2,0), (3,0), (4,0), (5,0)],  # ----
    1: [(2,1), (3,1), (4,1), (3,2), (3,0)],  # +
    2: [(2,2), (3,2), (4,2), (4,1), (4,0)],  # J
    3: [(2,0), (2,1), (2,2), (2,3)],  # I
    4: [(2,1), (3,1), (2,0), (3,0)]  # #
}

rock_height = {
    0: 1,  # ----
    1: 3,  # +
    2: 3,  # J
    3: 4,  # I
    4: 2  # #
}


def push(chamber, rock, direction):
    new_rock = []
    for pos in rock:
        x, y = pos
        new_x = x + direction
        if new_x < 0 or new_x > 6:
            return rock

        if chamber[y][new_x] != '.':
            return rock

        new_rock.append((new_x, y))

    return new_rock


def fall(chamber, rock):
    new_rock = []
    for pos in rock:
        x, y = pos
        new_y = y + 1
        if new_y < 0 or new_y >= len(chamber):
            return None

        if chamber[new_y][x] != '.':
            return None

        new_rock.append((x, new_y))

    return new_rock


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    jet = [c for c in lines[0].strip()]

    blank = ['.' for _ in range(7)]
    chamber = []
    highest = [0 for _ in range(7)]
    counter = 0
    profile_cache, high_cache = [], []
    tmp_profile, tmp_highest = [], []
    end = 2022 if stage == 1 else 1000000000000
    save_period = 5

    for i in range(end):
        tmp_profile.append(tuple([h - min(highest) for h in highest]))
        tmp_highest.append(max(highest))
        if i % save_period == 0:
            if (prof := tuple(tmp_profile)) not in profile_cache:
                profile_cache.append(prof)
                high_cache.append(tuple(tmp_highest))
            else:
                index = profile_cache.index(prof)
                begin_height = high_cache[index][-1]
                height_diff = max(highest) - begin_height
                rest = end - i
                period_mult = rest // (i - index*save_period)
                rest = rest % (i - index*save_period) - 1
                new_i = index + rest // save_period + 1
                inner_i = rest % save_period
                result = max(highest) + period_mult * height_diff + (high_cache[new_i][inner_i] - begin_height)
                print(result)
                break

            tmp_profile.clear()
            tmp_highest.clear()

        spawn = max(highest) + 3
        while len(chamber) < spawn:
            chamber.insert(0, blank.copy())

        rock_index = i % 5
        rock = rocks[rock_index]
        height = spawn + rock_height[rock_index]
        while len(chamber) < height:
            chamber.insert(0, blank.copy())

        rock = [(r[0], r[1] + (len(chamber) - height)) for r in rock]

        while True:
            push_dir = jet[counter % len(jet)]
            counter += 1
            rock = push(chamber, rock, 1 if push_dir == '>' else -1)
            new_rock = fall(chamber, rock)
            if new_rock is None:
                break
            rock = new_rock


        bottom = len(chamber)
        for pos in rock:
            highest[pos[0]] = (bottom - pos[1]) if (bottom - pos[1]) > highest[pos[0]] else highest[pos[0]]
            chamber[pos[1]][pos[0]] = '#'
    else:
        print(max(highest))

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
