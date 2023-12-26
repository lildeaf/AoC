import time
import math

def intersection_xy(p1, v1, p2, v2, start, end):
    x1, y1 = p1[0], p1[1]
    vx1, vy1 = v1[0], v1[1]
    x2, y2 = p2[0], p2[1]
    vx2, vy2 = v2[0], v2[1]

    t1 = (y1 * vx2 + vy2 * x2 - y2 * vx2 - x1 * vy2) / (vx1 * vy2 - vy1 * vx2)
    if t1 < 0:
        return False

    t2 = (x1 + vx1 * t1 - x2) / vx2
    if t2 < 0:
        return False

    inters1 = (x1 + vx1 * t1, y1 + vy1 * t1)
    return inters1[0] > start and inters1[1] > start and inters1[0] < end and inters1[1] < end


def cross(v1, v2):
    res = (v1[1] * v2[2] - v1[2] * v2[1],
           v1[2] * v2[0] - v1[0] * v2[2],
           v1[0] * v2[1] - v1[1] * v2[0])

    return res


def get_intersect(p1, v1, p2, v2):
    g = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])

    k = cross(v2, v1)
    h = cross(v2, g)

    kl = math.sqrt(math.pow(k[0], 2) + math.pow(k[1], 2) + math.pow(k[2], 2))
    hl = math.sqrt(math.pow(h[0], 2) + math.pow(h[1], 2) + math.pow(h[2], 2))

    if hl == 0 or kl == 0:
        return None
    tmp = (hl / kl)
    l = (v1[0] * tmp, v1[1] * tmp, v1[2] * tmp)
    res = (round(p1[0] + l[0]), round(p1[1] + l[1]), round(p1[2] + l[2]))
    return res


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    stones = []
    test_start = 7 if testing else 200000000000000
    test_end = 21 if testing else 400000000000000

    for line in lines:
        position, velocity = line.strip().split('@')
        x, y, z = [int(c) for c in position.split(',')]
        vx, vy, vz = [int(c) for c in velocity.split(',')]
        stone = ((x, y, z), (vx, vy, vz))
        stones.append(stone)

    intersections = []
    checks_x = set()
    checks_y = set()
    checks_z = set()

    #stage 1
    for i, stone in enumerate(stones):
        stone1, velocity1 = stone
        for j in range(i + 1, len(stones)):
            stone2, velocity2 = stones[j]
            if stone2[0] > stone1[0] and velocity2[0] > velocity1[0]:
                new_range = list(range(velocity1[0], velocity2[0]))
                checks_x.update(new_range)
            if stone2[1] > stone1[1] and velocity2[1] > velocity1[1]:
                new_range = list(range(velocity1[1], velocity2[1]))
                checks_y.update(new_range)
            if stone2[2] > stone1[2] and velocity2[2] > velocity1[2]:
                new_range = list(range(velocity1[2], velocity2[2]))
                checks_z.update(new_range)

            # parallel check
            r1 = velocity1[0] / velocity2[0]
            r2 = velocity1[1] / velocity2[1]

            if r1 == r2:
                continue

            if intersection_xy(stone1, velocity1, stone2, velocity2, test_start, test_end):
                intersections.append((i, j))

    if stage == 1:
        print("Stage 1:", len(intersections))
        return

    ranges = 300
    for rock_x in range(-ranges, ranges):
        if rock_x in checks_x:
            continue
        for rock_y in range(-ranges, ranges):
            if rock_y in checks_y:
                continue
            for rock_z in range(-ranges, ranges):
                if rock_z in checks_z:
                    continue
                rock = (rock_x, rock_y, rock_z)
                collision = None
                for i in range(1, len(stones)):
                    hailstone1 = stones[i]
                    pos1, vel1 = hailstone1
                    hailstone2 = stones[i - 1]
                    pos2, vel2 = hailstone2
                    vel1 = (vel1[0]-rock[0], vel1[1]-rock[1], vel1[2]-rock[2])
                    vel2 = (vel2[0]-rock[0], vel2[1]-rock[1], vel2[2]-rock[2])
                    hit = get_intersect(pos1, vel1, pos2, vel2)
                    if hit == None:
                        break
                    if collision == None:
                        collision = hit
                        continue
                    if not hit == collision:
                        break
                else:
                    print("found velocity and initial position:", rock, collision)
                    print("Stage 2:", sum(collision))
                    return


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
