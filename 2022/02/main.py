import time

def outcome(opp, own):
    opp_num = ord(opp) - ord('A')
    own_num = ord(own) - ord('X')
    if stage == 2:
        return own_num*3

    if opp_num == own_num:
        return 3

    return 6 if (own_num - 1) % 3 == opp_num else 0


def shape_score(opp, shape):
    if stage == 1:
        return ord(shape) - ord('W')

    opp_num = ord(opp) - ord('A')
    own_num = ord(shape) - ord('X')

    return ((opp_num + (own_num - 1)) % 3) + 1


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    rounds = []
    for line in lines:
        rounds.append(outcome(line[0], line[2]) + shape_score(line[0], line[2]))

    print(sum(rounds))

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
