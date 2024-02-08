import time

def update_worry(old, op):
    op1 = old if op[0] == 'old' else int(op[0])
    op2 = old if op[2] == 'old' else int(op[2])

    if op[1] == '+':
        return op1 + op2

    if op[1] == '*':
        return op1 * op2

    if op[1] == '-':
        return op1 - op2

    if op[1] == '/':
        return op1 / op2



def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    monkeys = []
    modulus = 1
    for i in range(0, len(lines), 7):
        items = [int(it.strip()) for it in lines[i+1].strip().split(':')[1].split(',')]
        operation = lines[i+2].strip().split('=')[1].split()
        test = int(lines[i+3].strip().split(':')[1].split()[-1])
        tr = int(lines[i+4].strip().split('monkey')[-1].strip())
        fal = int(lines[i+5].strip().split('monkey')[-1].strip())
        modulus *= test

        monkey = {
                    'items': items,
                    'op': operation,
                    'test': test,
                    't': tr,
                    'f': fal
                }
        monkeys.append(monkey)

    inspections = [0 for _ in monkeys]
    for r in range(20 if stage == 1 else 10000):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for it in monkey['items']:
                mod = monkey['test']
                new_val = update_worry(it, monkey['op'])
                if stage == 1:
                    new_val /= 3
                    new_val = int(new_val)
                else:
                    new_val %= modulus

                if new_val % mod == 0:
                    monkeys[monkey['t']]['items'].append(new_val)
                else:
                    monkeys[monkey['f']]['items'].append(new_val)
            inspections[i] = inspections[i] + len(monkey['items'])
            monkey['items'].clear()

    print(inspections)
    inspections.sort()
    print(inspections[-1] * inspections[-2])

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
