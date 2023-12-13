import time
import re

from functools import cmp_to_key

example = [
    "seeds: 79 14 55 13\n",
    "\n",
    "seed-to-soil map:\n",
    "50 98 2\n",
    "52 50 48\n",
    "\n",
    "soil-to-fertilizer map:\n",
    "0 15 37\n",
    "37 52 2\n",
    "39 0 15\n",
    "\n",
    "fertilizer-to-water map:\n",
    "49 53 8\n",
    "0 11 42\n",
    "42 0 7\n",
    "57 7 4\n",
    "\n",
    "water-to-light map:\n",
    "88 18 7\n",
    "18 25 70\n",
    "\n",
    "light-to-temperature map:\n",
    "45 77 23\n",
    "81 45 19\n",
    "68 64 13\n",
    "\n",
    "temperature-to-humidity map:\n",
    "0 69 1\n",
    "1 0 69\n",
    "\n",
    "humidity-to-location map:\n",
    "60 56 37\n",
    "56 93 4\n"
]


def compare(item1, item2):
    if item1[1] < item2[1]:
        return -1
    return 1


def compare1(item1, item2):
    if item1[0] < item2[0]:
        return -1
    return 1


def makeIt(mappings, nums_p):
    nums = nums_p
    new_nums = []

    for mapping in mappings:
        entries = mapping
        new_nums.clear()
        num_i = 0
        entries_index = 0
        while num_i < len(nums):
            if entries_index == len(entries):
                break
            dest_start, src_start, map_range = entries[entries_index]
            src_end = src_start + map_range

            num = nums[num_i]
            num_start, num_range = num
            num_end = num_start + num_range

            # all nums not in mapping
            if num_end < src_start:
                new_nums.append(num)
                nums.pop(num_i)
                continue

            # nums not in mapping yet
            if num_start >= src_end:
                entries_index += 1
                continue

            # end part of nums in mapping
            if num_start < src_start < num_end < src_end:
                new_nums.append([num_start, src_start - num_start])
                new_range = num_end - src_start
                nums[num_i] = [src_start, new_range]
                continue

            # start part of nums in mapping
            if src_start <= num_start < src_end:
                # all of nums in mapping
                if num_end <= src_end:
                    new_nums.append([dest_start + (num_start - src_start), num_range])
                    nums.pop(num_i)
                else:
                    new_range = src_end - num_start
                    new_nums.append([dest_start + (num_start - src_start), new_range])
                    nums[num_i] = [num_start + new_range, num_range - new_range]
                continue

            if len(nums) == 0:
                break
            num_i += 1

        new_nums.extend(nums)
        nums = sorted(new_nums.copy(), key=cmp_to_key(compare1))
        # print(nums)

    return nums[0]


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()
    if testing:
        lines = example

    pattern = re.compile("\d+")

    nums = [int(x.group()) for x in pattern.finditer(lines[0])]

    mappings = re.split(".*:", "".join(lines[2:]))
    gibMappings = []

    for mapping in mappings:
        if len(mapping) == 0:
            continue

        single_mappings = mapping.split("\n")
        entries = []
        for single_mapping in single_mappings:
            if len(single_mapping) == 0:
                continue

            entries.append([int(x) for x in single_mapping.split()])

        entries = sorted(entries, key=cmp_to_key(compare))
        gibMappings.append(entries)

    new_nums = []
    if stage == 1:
        for num in nums:
            new_nums.append([num, 1])
        solution = makeIt(gibMappings, sorted(new_nums, key=cmp_to_key(compare1)))
        print("SMALL:", solution[0])
    else:
        for i in range(0, len(nums), 2):
            new_nums.append([nums[i], nums[i + 1]])
            pass
        solution = makeIt(gibMappings, sorted(new_nums, key=cmp_to_key(compare1)))
        print("SMALL:", solution[0])


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
