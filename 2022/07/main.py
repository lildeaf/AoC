import time

def handle_ls(lines, index):
    sum = 0
    while index < len(lines):
        line = lines[index]
        comp = line.split()
        if comp[0] == '$':
            return sum, index
        if comp[0] == 'dir':
            index += 1
            continue
        sum += int(comp[0])
        index += 1

    return sum, index

def handle_directory(lines, current_path, directories, index):
    sum = 0
    while index < len(lines):
        line = lines[index]
        comp = line.split()
        if comp[0] != '$':
            index += 1
            continue
        if comp[1] == 'ls':
            ls_sum, index = handle_ls(lines, index+1)
            sum += ls_sum
            continue
        if comp[1] == 'cd':
            if comp[2] == '..':
                directories['/'.join(current_path)] = sum
                return index+1
            else:
                current_path.append(comp[2])
                index = handle_directory(lines, current_path, directories, index+1)
                sum += directories['/'.join(current_path)]
                current_path.pop(-1)

    directories['/'.join(current_path)] = sum
    return index


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    directories = {}
    current_dir = ['/']
    handle_directory(lines, current_dir, directories, 1)
    space = directories['/']
    free_space = 70000000 - space

    sizes = []
    for v in directories.values():
        if stage == 1 and v < 100000:
            sizes.append(v)
        if stage == 2 and v > (30000000 - free_space):
            sizes.append(v)

    print(directories)
    print(sum(sizes) if stage == 1 else min(sizes))

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
