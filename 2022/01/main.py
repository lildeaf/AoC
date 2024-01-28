import time


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    elves = []
    sums = 0
    for line in lines:
        num = line.strip()
        if len(num) == 0:
            elves.append(sums)
            sums = 0
            continue 
        sums += int(num)
    else:
        elves.append(sums)

    elves.sort(reverse=True)
    top = 3 if stage == 2 else 1
    print(sum(elves[0:top]))


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
