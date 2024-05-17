import time

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    sensors, beacons = [], []

    for line in lines:
        sensor, beacon = line.strip().split(':')
        sensor, beacon = sensor[10:].split(','), beacon[22:].split(',')
        sens_x, sens_y = [coord.split('=')[1] for coord in sensor]
        beac_x, beac_y = [coord.split('=')[1] for coord in beacon]

        sensors.append((int(sens_x), int(sens_y)))
        beacons.append((int(beac_x), int(beac_y)))

    y_low = (10 if testing else 2000000) if stage == 1 else 0
    y_high = y_low + 1 if stage == 1 else (20 if testing else 4000000)

    print(y_low, y_high)

    for y_coord in range(y_low, y_high):
        ranges = []
        count = 0
        b_set = set()
        for i, sensor in enumerate(sensors):
            beacon = beacons[i]
            if sensor[1] == y_coord:
                count -= 1
            if beacon[1] == y_coord and beacon not in b_set:
                b_set.add(beacon)
                count -= 1

            diff_x = abs(sensor[0] - beacon[0])
            diff_y = abs(sensor[1] - beacon[1])
            distance = diff_x + diff_y
            min_y = sensor[1] - distance
            max_y = sensor[1] + distance
            if min_y <= y_coord <= max_y:
                y_diff = abs(y_coord - sensor[1])
                left = (sensor[0] - distance) + y_diff
                right = (sensor[0] + distance) - y_diff
                j = 0
                while j < len(ranges):
                    r_left, r_right = ranges[j]
                    if (right < r_left) or (left > r_right):# no overlap
                        j += 1
                        continue
                    if r_left <= left <= right <= r_right:# fully inside
                        break
                    if left <= r_left <= r_right <= right:# fully inside
                        ranges.pop(j)
                        continue

                    if r_left <= right <= r_right: #update start
                        ranges.pop(j)
                        left, right = left, r_right
                        continue
                    if r_left <= left <= r_right: #update end
                        ranges.pop(j)
                        left, right = r_left, right
                        continue
                else:
                    ranges.append((left, right))

        if stage == 1:
            for r in ranges:
                count += (r[1] - r[0]) + 1

            print(count)
        else:
            if len(ranges) > 1:
                found_x = 0
                for r in ranges:
                    found_x = (r[0] - 1) if (0 < r[0] < y_high) else found_x
                    found_x = (r[1] + 1) if (0 < r[1] < y_high) else found_x
                print(4000000 * found_x + y_coord)
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
