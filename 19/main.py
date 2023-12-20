import time
import re


def evaluate_part(part):
    if stage == 1:
        result = sum(part.values())
    else:
        result = 1
        for p in part.values():
            result *= ((p[1] - p[0]) + 1)
    return result


def evaluate_rule(rule, part):
    if rule[1] == '<':
        return part[rule[0]] < rule[2]
    else:
        return part[rule[0]] > rule[2]


def check_workflow(state, workflows, part):
    rules = workflows.get(state, None)
    if rules == None:
        return 0 if state == 'R' else evaluate_part(part)
    for rule in rules:
        if (state := rule[0]) and len(rule) == 1:
            return check_workflow(state, workflows, part)

        if evaluate_rule(rule, part):
            state = rule[3]
            return check_workflow(state, workflows, part)


def evaluate_rule_range(rule, part): #return True part, False part
    category, comparator, num, _ = rule
    part_start, part_end = part[category]
    if comparator == '<':
        if part_end < num:
            return part, None
        if part_start >= num:
            return None, part

        true_start = part_start
        true_end = num - 1
        false_start = num
        false_end = part_end
    else: # >
        if part_start > num:
            return part, None
        if part_end <= num:
            return None, part

        true_start = num + 1
        true_end = part_end
        false_start = part_start
        false_end = num

    true_part = {k: ([true_start, true_end] if k == category else v.copy()) for k, v in part.items()}
    false_part = {k: ([false_start, false_end] if k == category else v.copy()) for k, v in part.items()}
    return true_part, false_part


def check_workflow_range(state, workflows, part):
    rules = workflows.get(state, None)
    if rules == None:
        return 0 if state == 'R' else evaluate_part(part)

    possibilities = 0
    tmp_part = part
    for rule in rules:
        if (state := rule[0]) and len(rule) == 1:
            possibilities += check_workflow_range(state, workflows, tmp_part)
            continue

        cur_part, tmp_part = evaluate_rule_range(rule, tmp_part)
        if cur_part != None:
            state = rule[3]
            possibilities += check_workflow_range(state, workflows, cur_part)
        if tmp_part == None:
            break

    return possibilities


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    workflow_regex = re.compile(r"(\w+)\{(.+)\}")
    part_regex = re.compile(r"([x|m|a|s])(.)(\d+):(.+)")
    workflows = {}
    i = 0
    while line := lines[i].strip():
        match = workflow_regex.search(line)
        rules = []
        for rule in match.group(2).split(','):
            rule_match = part_regex.search(rule)
            if rule_match == None:
                rules.append((rule,))
                continue

            rules.append((rule_match.group(1), rule_match.group(2), int(rule_match.group(3)), rule_match.group(4)))
        i += 1
        workflows[match.group(1)] = rules

    if stage == 2:
        possible_parts = {p: [1, 4000] for p in 'xmas'}
        test = check_workflow_range("in", workflows, possible_parts)
        print("Stage 2:", test)
        return

    i += 1
    results = []
    for part in lines[i:]:
        part_dict = {p[0]: int(p[2:]) for p in part.strip()[1:-1].split(',')}
        res = check_workflow("in", workflows, part_dict)
        results.append(res)

    print("Stage 1:", sum(results))


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