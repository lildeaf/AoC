import time
import re

def getNextNumber(nums):
    if all([num == 0 for num in nums]):
        return 0

    next_nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    return (nums[-1] + getNextNumber(next_nums)) if stage == 1 else nums[0] - getNextNumber(next_nums)

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    lines = [[int(x) for x in re.findall('-?\d+', line)] for line in lines]

    new_nums = [getNextNumber(line) for line in lines]

    print("RESULT: ", sum(new_nums))

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