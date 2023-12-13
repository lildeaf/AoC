import time
import re
import math


def getNodes(lines, index):
    if index >= len(lines):
        return None

    return re.findall('\w+', lines[index])


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    steps = lines[0].strip('\n')
    total_steps = len(steps)
    nodes = {match[0]: (match[1], match[2]) for i in range(2, len(lines)) if (match := getNodes(lines, i))}

    current_nodes = ["AAA"] if stage == 1 else [node for node in nodes.keys() if node.endswith('A')]
    counters = [0] * len(current_nodes)
    counter = 0
    while (index := 0) or len(current_nodes) > 0:
        step = steps[counter % total_steps]
        counter += 1
        direction = 0 if step == 'L' else 1

        while index < len(current_nodes):
            if (current_node := current_nodes[index]).endswith('Z'):
                current_nodes.remove(current_node)
                continue
            else:
                next_node = nodes.get(current_node)[direction]
                current_nodes[index] = next_node
                index += 1

        # current_nodes = [nodes.get(current_nodes[i])[direction] for i in range(len(current_nodes)) if not current_nodes[i].endswith('Z')]
        counters = [counter if i < len(current_nodes) else counters[i] for i in range(len(counters))]

    common = 1
    while len(counters) > 0 and (num := counters[0]):
        common = math.lcm(common, num)
        counters.pop(0)

    print(common)


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
