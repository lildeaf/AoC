import time

def draw_CRT(cycle, reg, CRT):
    row = (cycle) // 40
    position = (cycle) % 40

    if reg - 1 <= position <= reg + 1:
        CRT[row].append('#')
    else:
        CRT[row].append('.')

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    register = 1
    cycle = 0
    signal = []
    CRT = [[] for _ in range(6)]

    for line in lines:
        instr = line.strip().split()
        if stage == 1:
            signal.append((cycle+1) * register)
        else:
            draw_CRT(cycle, register, CRT)

        if instr[0] == "noop":
            cycle += 1
            continue

        cycle += 1
        if stage == 1:
            signal.append((cycle + 1) * register)
        else:
            draw_CRT(cycle, register, CRT)

        cycle += 1
        register += int(instr[1])

    if stage == 1:
        signal_sum = 0
        for i in range(20, 221, 40):
            signal_sum += signal[i-1]
        print(signal_sum)
    else:
        for row in CRT:
            print(''.join(row))



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
