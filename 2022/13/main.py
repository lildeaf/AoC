import time
from functools import cmp_to_key

def check(p1, p2):
    l1 = len(p1)
    l2 = len(p2)

    for i in range(l1):
        if i >= l2:
            return False, False

        e1 = p1[i]
        e2 = p2[i]
        type1 = type(e1) is int
        type2 = type(e2) is int

        if type1 and type2:
            if e1 == e2:
                continue
            elif e1 < e2:
                return True, False
            else:
                return False, False

        if type1:
            e1 = [e1]
        if type2:
            e2 = [e2]

        correct, len_equal = check(e1, e2)
        if not correct:
            return False, False
        else:
            if len_equal:
                continue
            else:
                return True, False

    return True, l1 == l2

def compare(item1, item2):
    correct, len_equal = check(item1, item2)
    return -1 if correct else 1


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    indices = []
    packets = []

    for i in range(0, len(lines), 3):
        pack1 = eval(lines[i].strip())
        pack2 = eval(lines[i+1].strip())
        packets.append(pack1)
        packets.append(pack2)
        if stage == 2:
            continue

        correct, len_equal = check(pack1, pack2)
        if correct:
            indices.append(i//3+1)

    if stage == 1:
        print(sum(indices))
        return

    div1 = [[2]]
    div2 = [[6]]
    packets.append(div1)
    packets.append(div2)
    packets = sorted(packets, key=cmp_to_key(compare))
    for i, p in enumerate(packets):
        if p == div1 or p == div2:
            indices.append(i+1)
    print(indices[0] * indices[1])

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
