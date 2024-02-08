import time

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    buffer = lines[0].strip()
    offset = 4 if stage == 1 else 14
    end = len(buffer) - (offset-1)
    for i in range(0, end):
        slice_end = i+offset
        test = set(buffer[i:slice_end])
        if len(test) == offset:
            print(slice_end)
            break


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
