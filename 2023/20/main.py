import re
import time
import math


def get_inputs(modules, module):
    inputs = []
    for m, v in modules.items():
        if module in (v if m == "broadcaster" else v[1]):
            inputs.append(m)

    return inputs


# checks if modules are in initial state again
def check_state(modules):
    for m, v in modules.items():
        if m == "broadcaster":
            continue

        if v[0] == "%":  # flip-flop
            if v[2]:
                return False

        if v[0] == "&":  # conjunction
            if all(True if p == 1 else False for p in v[2].values()):
                return False

    return True


def get_rx_inf(modules):
    module_inputs = None
    for m, v in modules.items():
        if m == "broadcaster":
            continue
        if "rx" in v[1]:
            module_inputs = modules[m][2]
            break
    if module_inputs == None:
        print("Should not happen")
        exit(-1)

    return {module: None for module in module_inputs.keys()}


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    modules = {}
    module_pattern = re.compile("(.+) -> (.+)")
    for line in lines:
        module_match = module_pattern.search(line.strip())
        module = module_match.group(1)
        outputs = module_match.group(2)
        if module == "broadcaster":
            modules[module] = outputs.split(', ')
            continue

        modules[module[1:]] = (module[0], outputs.split(', '))

    for module, v in modules.items():
        if module == "broadcaster":
            continue

        if v[0] == "%":  # flip-flop
            new_v = v + (False,)
            modules[module] = new_v

        if v[0] == "&":  # conjunction
            inputs = get_inputs(modules, module)
            new_v = v + ({i: 0 for i in inputs},)
            modules[module] = new_v

    rx_inputs = get_rx_inf(modules) if not testing else {}

    pulses_per_press = {i: [0, 0] for i in range(0, 1001)}
    cycle = 1000
    max_cycles = 10000
    for press in range(1, max_cycles+1):
        pulses = [("btn", 0, "broadcaster")]
        sent_pulses = [0, 0]
        while len(pulses) > 0:
            pulse = pulses.pop(0)
            sender, pulse_type, module_name = pulse
            sent_pulses[pulse_type] = sent_pulses[pulse_type] + 1
            if stage == 2 and module_name == "rx":
                send = modules[sender]
                if all(True if p != None else False for p in rx_inputs.values()):
                    common = 1
                    gib = list(rx_inputs.values()).copy()
                    while len(gib) > 0 and (num := gib[0]):
                        common = math.lcm(common, num)
                        gib.pop(0)

                    print("Stage 2:", common)
                    return

                for k, v in send[2].items():
                    if v == 0:
                        continue

                    if rx_inputs.get(k) == None:
                        rx_inputs[k] = press

            module = modules.get(module_name, None)
            if module == None:
                continue
            if module_name == "broadcaster":
                for m in module:
                    pulses.append((module_name, 0, m))
                continue

            if module[0] == '%':  # flip-flop
                if pulse_type == 1:
                    continue

                new_state = not module[2]  # flip state
                new_mod = module[:-1] + (new_state,)
                modules[module_name] = new_mod
                pulse_type = 1 if new_state else 0
                for m in module[1]:
                    pulses.append((module_name, pulse_type, m))
                continue

            if module[0] == "&":  # conjunction
                inputs = module[2]
                inputs[sender] = pulse_type  # update state
                new_mod = module[:-1] + (inputs,)
                modules[module_name] = new_mod
                pulse_type = 0 if all(True if p == 1 else False for p in inputs.values()) else 1
                for m in module[1]:
                    pulses.append((module_name, pulse_type, m))
                continue

        if stage == 1:
            init_state = check_state(modules)
            prev = pulses_per_press[press - 1]
            pulses_per_press[press] = [prev[0] + sent_pulses[0], prev[1] + sent_pulses[1]]
            if init_state or press == 1000:
                cycle = press
                break

    max_cycles = 1000
    lows, highs = pulses_per_press[cycle]
    multiplier = max_cycles // cycle
    mod = max_cycles % cycle
    lows_rem, highs_rem = pulses_per_press[mod]
    print("Stage 1:", (lows*multiplier + lows_rem) * (highs*multiplier + highs_rem))


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
