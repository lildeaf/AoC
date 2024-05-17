import time

cache = {}
def dfs(connections, rates, current, counter, opened, elephant = 0):
    if counter >= 30:
        return 0 if elephant == 0 else dfs(connections, rates, 'AA', 5, opened, 0)

    if (pressure := cache.get((current, counter, frozenset(opened), elephant), None)) is not None:
        return pressure

    rate = rates[current]
    max_pressure = 0
    if rate > 0 and current not in opened:
        opened.add(current)
        press = dfs(connections, rates, current, counter + 1, opened, elephant)
        press += (rate * (30 - counter))
        max_pressure = press if press > max_pressure else max_pressure
        opened.discard(current)

    conns = connections[current]
    for conn in conns:
        press = dfs(connections, rates, conn, counter + 1, opened, elephant)
        max_pressure = press if press > max_pressure else max_pressure

    cache[(current, counter, frozenset(opened), elephant)] = max_pressure

    return max_pressure

def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    connections = {}
    rates = {}

    for line in lines:
        valve, tunnels = line.strip().split(';')
        tag, rate = valve.split('=')
        tag = tag.split()[1]
        rates[tag] = int(rate)
        tunnels = tunnels.split(',')
        tunnels[0] = tunnels[0][-2:]
        tunnels = [t.strip() for t in tunnels]
        connections[tag] = tunnels

    if stage == 1:
        cache.clear()
        max_pressure = dfs(connections, rates, 'AA', 1, set())
        print(max_pressure)
    else:
        cache.clear()
        max_pressure = dfs(connections, rates, 'AA', 5, set(), 1)
        print(max_pressure)


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
