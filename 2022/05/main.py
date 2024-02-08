import time

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    stacks = {}

    for i in range(len(lines)):
        if lines[i].strip() == '':
            break

        for index, c in enumerate(lines[i]):
            if c.isupper():
                stack_num = (index // 4) + 1
                stack = stacks.get(stack_num, [])
                stack.append(c)
                stacks[stack_num] = stack

    for proc in lines[i+1:]:
        nums = [int(c) for c in proc.split()[1::2]]
        stack_src = stacks.get(nums[1], [])
        stack_dst = stacks.get(nums[2], [])

        to_move = stack_src[0:nums[0]]
        if stage == 1:
            to_move.reverse()
        stack_dst = to_move + stack_dst
        stack_src = stack_src[nums[0]:]

        stacks[nums[1]] = stack_src
        stacks[nums[2]] = stack_dst

    top = ''
    for k in sorted(stacks.keys()):
        top += stacks[k][0]

    print(top)


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
