import time

def check_vertical(lines, stage):
    for x in range(1, len(lines[0])):
        refl = []
        for line in lines:
            if refl.count(False) > 1:
                break

            left_part = line[:x][::-1]
            right_part = line[x:]

            if len(left_part) < len(right_part):
                refl.append(right_part.startswith(left_part))
            else:
                refl.append(left_part.startswith(right_part))

        if stage == 1 and all(refl):
            return x
        if stage == 2 and refl.count(False) == 1:
            return x

    return -1


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    lines = [part.split('\n') for part in ''.join(lines).split('\n\n')]
    results = []
    for part in lines:
        if (tmp := check_vertical(part, stage)) != -1:
            results.append(tmp)
        else:
            transposed = [''.join(x) for x in list(map(list, zip(*part)))]
            results.append(check_vertical(transposed, stage) * 100)

    print(sum(results))


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