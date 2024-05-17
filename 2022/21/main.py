import time

reverse = {
    '+' : '-',
    '-': '+',
    '*': '/',
    '/': '*'
}

def operation(n1, op, n2):

    if op == '+':
        return n1 + n2

    if op == '-':
        return n1 - n2

    if op == '*':
        return int(n1 * n2)

    if op == '/':
        return int(n1 / n2)


def rec(monkeys, current):
    yell = monkeys[current]

    if len(yell) == 1:
        return yell[0]

    monkey1, op, monkey2 = yell
    monkey1 = rec(monkeys, monkey1)
    monkey2 = rec(monkeys, monkey2)

    res = operation(monkey1, op, monkey2)
    return res


def rec2(monkeys, current):
    yell = monkeys[current]

    if len(yell) == 1:
        return (current, yell[0])

    monkey1, op, monkey2 = yell
    monkey1 = rec2(monkeys, monkey1)
    monkey2 = rec2(monkeys, monkey2)

    return (monkey1, op, monkey2)


def resolve(x):
    if len(x) == 2:
        return x[1] if x[0] != 'humn' else None

    m1 = resolve(x[0])
    m2 = resolve(x[2])

    return operation(m1, x[1], m2) if m1 is not None and m2 is not None else None


def reverse_resolve(x, num):
    if len(x) == 2:
        return x[1] if x[0] != 'humn' else num

    m1 = resolve(x[0])
    m2 = resolve(x[2])

    if m1 is None: #m2 is number
        new_x = x[0]
        new_num = operation(num, reverse[x[1]], m2)
    else: #m1 is number
        new_x = x[2]
        if x[1] == '+' or x[1] == '*':
            new_num = operation(num, reverse[x[1]], m1)
        elif x[1] == '-':
            new_num = -1 * (num - m1)
        else:  # /
            new_num = m1 / num

    return reverse_resolve(new_x, new_num)


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    monkeys = {}

    for line in lines:
        name, yell = line.strip().split(':')
        yell = yell.split()
        test = tuple([int(n) if n.isdigit() else n for n in yell])
        monkeys[name] = test

    if stage == 1:
        result = rec(monkeys, 'root')
        print(result)
    else:
        test = rec2(monkeys, 'root')

        m1 = resolve(test[0])
        m2 = resolve(test[2])

        result = reverse_resolve(test[0] if m1 is None else test[2], m2 if m1 is None else m1)
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
