import time
import re
import functools

@functools.cache
def rec_group(g, curr_index, spans, count, dot_seq=True):
    possible = 0

    if curr_index >= len(g):
        if len(spans) == 0:
            return 0 if count > 0 else 1
        else:
            return 1 if len(spans) == 1 and spans[0] == count else 0

    if g[curr_index] == '#':
        if len(spans) > 0 and count < spans[0]:
            if dot_seq:
                possible += rec_group(g, curr_index + 1, spans, count + 1, False)
            else:
                possible += rec_group(g, curr_index + 1, spans, count + 1, False)

    if g[curr_index] == '.':
        tmp_pos = 0
        if not dot_seq:
            if len(spans) > 0 and spans[0] == count:
                tmp_pos += rec_group(g, curr_index+1, spans[1:], 0)
        else:
            tmp_pos += rec_group(g, curr_index+1, spans, count)

        possible += tmp_pos

    if g[curr_index] == '?':
        tmp_pos = 0
        if len(spans) > 0 and count < spans[0]:
            if dot_seq:
                tmp_pos += rec_group(g, curr_index + 1, spans, count + 1, False)  # same as hashtag
            else:
                tmp_pos += rec_group(g, curr_index + 1, spans, count + 1, False)  # same as hashtag

        if not dot_seq:
            if len(spans) > 0 and spans[0] == count:
                tmp_pos += rec_group(g, curr_index+1, spans[1:], 0)
        else:
            tmp_pos += rec_group(g, curr_index+1, spans, count)

        possible += tmp_pos

    return possible


def handle_groups(g, spans):
    poss = rec_group(g, 0, spans, 0)
    return poss

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    arrangem = []
    counter = 1
    for line in lines:
        spans = [int(x) for x in re.findall("\d+", line)]
        spans = tuple(spans)
        row = line.split()[0]
        if stage == 2:
            test = '?'.join([row] * 5)
            poss = handle_groups(test, spans * 5)
        else:
            poss = handle_groups(row, spans)

        counter += 1
        arrangem.append(poss)

    print(sum(arrangem))

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