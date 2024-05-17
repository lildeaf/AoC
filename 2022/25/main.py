import time


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]

    results = 0
    for line in lines:
        nums = []
        for i, c in enumerate(line[::-1]):
            num = 5**i
            if c == '-':
                nums.append(-num)
                continue
            if c == '=':
                nums.append(-2*num)
                continue
            nums.append(int(c)*num)
        results += sum(nums)

    snafu = []
    carry = 0
    while results > 0:
        digit = (results % 5) + carry
        results = results // 5
        carry = 0
        if digit < 3:
            snafu.append(str(digit))
            continue

        if digit == 3:
            snafu.append('=')

        if digit == 4:
            snafu.append('-')

        if digit == 5:
            snafu.append('0')

        carry = 1

    print(''.join(snafu[::-1]))


if __name__ == '__main__':
    testing = False
    stage = 1
    start = time.time()
    task()
    print(time.time() - start)
    stage = 2
    start = time.time()
    #task()
    print(time.time() - start)
