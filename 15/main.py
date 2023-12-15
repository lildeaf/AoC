import time
import re


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    steps = lines[0].split(',')
    results = []
    boxes = {i: [] for i in range(256)}
    for step in steps:
        label, op, focal = re.split('([-|=])', step)
        label_hash = 0
        for c in (label if stage == 2 else step):
            label_hash = ((label_hash + ord(c)) * 17) % 256

        box = boxes[label_hash]
        for i, lens in enumerate(box):
            if lens[0] != label:
                continue

            if op == '-':
                box.pop(i)
            else:
                box[i] = (label, int(focal))
            break
        else:
            if op == '=':
                box.append((label, int(focal)))

        boxes[label_hash] = box
        results.append(label_hash)
    if stage == 1:
        print("STAGE 1: ", sum(results))
        return

    results.clear()
    for box_index, box in boxes.items():
        results.extend([lens[1] * (lens_index + 1) * (box_index + 1) for lens_index, lens in enumerate(box)])

    print("STAGE 2: ", sum(results))


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
