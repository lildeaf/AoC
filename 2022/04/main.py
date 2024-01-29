import time

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    pairs = []
    for line in lines:
        sec1, sec2 = line.strip().split(',')
        range1 = [int(num) for num in sec1.split('-')]
        range2 = [int(num) for num in sec2.split('-')]
        if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range2[0] <= range1[0] and range2[1] >= range1[1]):
            pairs.append(1)
            continue

        if stage == 2 and not (range1[1] < range2[0] or range1[0] > range2[1]):
            pairs.append(1)

    print(sum(pairs))

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
