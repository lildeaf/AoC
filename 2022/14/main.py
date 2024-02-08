import time

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    tmp = ['.'] * 500
    scan = []
    lowest = 0
    for _ in range(500):
        scan.append(tmp.copy())
    scan[0][250] = '+'

    for line in lines:
        coords = line.strip().split("->")
        current = [int(x) for x in coords[0].strip().split(',')]
        for coord in coords:
            dest = [int(x) for x in coord.strip().split(',')]
            x_diff = dest[0] - current[0]
            y_diff = dest[1] - current[1]
            y = current[1]

            for i in range(0, x_diff, -1 if x_diff < 0 else 1):
                x = (current[0] + i) - 250
                y = current[1]
                scan[y][x] = '#'

            for i in range(0, y_diff, -1 if y_diff < 0 else 1):
                x = current[0] - 250
                y = current[1] + i
                scan[y][x] = '#'

            if y > lowest:
                lowest = y

            current = dest

        scan[current[1]][current[0]-250] = '#'

    if stage == 2:
        scan[lowest+2] = ['#'] * 500

    counter = 0
    while True:
        sand = [0, 250]
        for i in range(498):
            if scan[sand[0]+1][sand[1]] == '.':
                sand[0] += 1
                continue
            if scan[sand[0]+1][sand[1]-1] == '.':
                sand[0] += 1
                sand[1] -= 1
                continue
            if scan[sand[0]+1][sand[1]+1] == '.':
                sand[0] += 1
                sand[1] += 1
                continue
            scan[sand[0]][sand[1]] = 'o'
            counter += 1
            if sand[0] == 0 and sand[1] == 250:
                print(counter)
                return
            break
            pass
        else:
            break

    print(counter)


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
