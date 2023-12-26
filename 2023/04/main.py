import time
import re


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    sums = 0
    instances = [1] * len(lines)

    for cardNumber, card in enumerate(lines):
        index = re.search(':', card).start()
        nums = card[index + 1:].split('|')
        winning_nums, my_nums = [int(x) for x in nums[0].split()], [int(x) for x in nums[1].split()]
        correct_nums = [1 for x in my_nums if x in winning_nums]

        if stage == 1:
            sums += int(pow(2, sum(correct_nums) - 1))
        else:
            instances[cardNumber + 1:cardNumber + len(correct_nums) + 1] = [
                instances[cardNumber] + instances[cardNumber + i + 1] for i, x in enumerate(correct_nums)]
            sums += instances[cardNumber]

    print(sums)


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
