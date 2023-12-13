import time
from functools import cmp_to_key

stage = 1


def get_hand_type(hand):
    dictl = {}
    for card in hand:
        if card in dictl:
            dictl[card] += 1
        else:
            dictl[card] = 1
    occs = sorted(dictl.values(), reverse=True)
    joker = dictl.get('#', 0)

    if stage == 2 and 0 < joker < 5:
        if joker == 1:
            occs[0] += 1
            occs = occs[:-1]
        else:
            occs[0] += occs[1]
            occs.pop(1)

    length = len(occs)
    return occs[0] ** 2 - length


def compare(item1, item2):
    hand1 = item1.split()[0]
    hand2 = item2.split()[0]

    type1 = get_hand_type(hand1)
    type2 = get_hand_type(hand2)

    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1
    else:
        return -1 if hand1 < hand2 else 1


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    subs = {
        'A': 'F',
        'K': 'E',
        'Q': 'D',
        'J': ('C' if stage == 1 else '#'),
        'T': 'B'
    }

    lines = ":".join(lines)
    for key, val in subs.items():
        lines = lines.replace(key, val)
    lines = lines.split(':')
    # lines = (":".join(lines).replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', 'C').replace('T', 'B')).split(':')
    lines = sorted(lines, key=cmp_to_key(compare))
    lines = ":".join(lines)
    for key, val in subs.items():
        lines.replace(val, key)
    # lines = (":".join(lines).replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')).split(':')
    lines = lines.split(':')
    lines = (":".join(lines).replace('A', 'T').replace('B', 'J').replace('C', 'Q').replace('D', 'K').replace('E',
                                                                                                             'A')).split(
        ':')

    winnings = 0
    for index, item in enumerate(lines):
        bid = int(item.split()[1])
        winnings += bid * (index + 1)

    print(winnings)


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
