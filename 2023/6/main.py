import time


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    if stage == 1:
        times = [int(x) for x in lines[0].split()[1:]]
        distances = [int(x) for x in lines[1].split()[1:]]
    else:
        times = [int(''.join(lines[0].split()[1:]))]
        distances = [int(''.join(lines[1].split()[1:]))]

    result = 1
    for race_time, distance in zip(times, distances):
        start_time = 0
        end_time = race_time
        num_check = start_time + (end_time - start_time) // 2
        while True:
            check1 = num_check * (race_time - num_check) > distance
            check2 = (num_check + 1) * (race_time - (num_check + 1)) > distance
            if not check1 and check2:
                break

            start_time, end_time = (start_time, num_check) if check1 and check2 else (num_check, end_time)
            num_check = start_time + (end_time - start_time) // 2

        i = num_check + 1
        result *= (race_time - i - (i - 1))
    print(result)


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
