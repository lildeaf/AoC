import time

def stage_one(rucksack):
    comp1 = rucksack[:len(rucksack) // 2]
    comp2 = rucksack[len(rucksack) // 2:]
    char = [ord(c) for c in comp1 if c in comp2][0]
    return (char - 0x40) + 26 if char < 0x60 else char - 0x60

def stage_two(rs1, rs2, rs3):
    char = [ord(c) for c in rs1 if c in rs2 and c in rs3][0]
    return (char - 0x40) + 26 if char < 0x60 else char - 0x60

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    items = []
    for i in range(0, len(lines), 1 if stage==1 else 3):
        items.append(stage_one(lines[i].strip()) if stage == 1 else stage_two(*lines[i:i+3]))

    print(sum(items))

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
