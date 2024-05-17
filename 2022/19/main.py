import time

cache = {}


def check_res(rid, cost, resources):
    if cost[0] > resources[0]: #not enough ore
        return None

    if rid < 2: #ore and clay only need ore
        new_res = resources.copy()
        new_res[0] -= cost[0]
        return new_res

    if rid == 2 and cost[1] <= resources[1]: #obsidian needs clay
        new_res = resources.copy()
        new_res[0] -= cost[0]
        new_res[1] -= cost[1]
        return new_res

    if rid == 3 and cost[1] <= resources[2]: #geode needs obsidian
        new_res = resources.copy()
        new_res[0] -= cost[0]
        new_res[2] -= cost[1]
        return new_res

    return None


def dfs_again(costs, maximums, robots, current_time, resources):
    if current_time == (24 if stage == 1 else 32):
        return resources

    if (res := cache.get((current_time, tuple(robots), tuple(resources)), None)) is not None:
        return res

    most_geode = resources.copy()
    for i, cost in enumerate(costs):
        if i < 3 and robots[i] >= maximums[i]:
            continue

        if (new_res := check_res(i, cost, resources)) is None:
            continue

        new_rob = robots.copy()
        new_rob[i] += 1
        for j, n in enumerate(robots):
            new_res[j] += n

        op = dfs_again(costs,  maximums, new_rob, current_time + 1, new_res)
        if op[3] > most_geode[3]:
            most_geode = op
    else:
        new_res = resources.copy()
        for j, n in enumerate(robots):
            new_res[j] += n
        op = dfs_again(costs,  maximums, robots.copy(), current_time + 1, new_res)
        if op[3] > most_geode[3]:
            most_geode = op

    key = (current_time, tuple(robots), tuple(resources))
    cache[key] = most_geode

    return most_geode


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    blueprints = {}
    bp_max = {}

    for line in lines:
        rid, blueprint = line.strip().split(':')
        rid = int(rid.split(' ')[1])
        robots = blueprint.strip().split('.')
        costs = []
        ore_max = 0
        clay_max = 0
        obs_max = 0
        for i in range(4):
            robot = robots[i]
            robot = robot.strip().split(' ')
            cost = (int(robot[4]),)
            if i > 0:
                ore_max = max(ore_max, int(robot[4]))
            if i > 1:
                cost += (int(robot[7]),)
                if i == 2:
                    clay_max = max(clay_max, int(robot[7]))
                else:
                    obs_max = max(obs_max, int(robot[7]))

            costs.append(cost)

        blueprints[rid] = tuple(costs)
        bp_max[rid] = tuple([ore_max, clay_max, obs_max])

    qualities = []
    prod = 1
    cache.clear()
    for k, v in blueprints.items():
        if stage == 2 and k > 3:
            continue
        res = dfs_again(v, bp_max[k], [1, 0, 0, 0], 0, [0, 0, 0, 0])
        qualities.append(res[-1] * k)
        prod *= res[-1]
        print(k, qualities[-1])
        cache.clear()

    print(qualities)
    print(sum(qualities) if stage == 1 else prod)


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
