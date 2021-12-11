import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    input = []
    for line in input_lines:
        nums = list(line.strip())
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        input.append(nums)
    return input


folder = "Day_9"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def is_min(x_pos, y_pos, map):
    for x in range(x_pos - 1, x_pos + 2):
        for y in range(y_pos - 1, y_pos + 2):
            if (x < 0 or x >= len(map[0])):
                continue
            if (y < 0 or y >= len(map)):
                continue
            if (y == y_pos and x == x_pos):
                continue
            if (map[y][x] <= map[y_pos][x_pos]):
                return False
    return True


def solve_p1():
    num_min = 0
    data = input_data
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (is_min(x, y, data)):
                num_min += 1 + data[y][x]
    print(num_min)


def in_bounds(x, y, map):
    if (x < 0 or x >= len(map[0])):
        return False
    if (y < 0 or y >= len(map)):
        return False
    return True


def dfs(x, y, v, map):
    basin = []
    q = [[x, y]]
    while (len(q) > 0):
        cur = q.pop()
        x = cur[0]
        y = cur[1]
        if (not in_bounds(x, y, map)):
            continue

        key = f"{x},{y}"
        if (key in v):
            continue
        v.add(key)

        if (map[y][x] < 9):
            basin.append(cur)
            q.append([x - 1, y])
            q.append([x + 1, y])
            q.append([x, y+1])
            q.append([x, y-1])
    return basin


def solve_p2():
    data = input_data
    basins = []
    v = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            basin = dfs(x, y, v, data)
            if (basin != []):
                basins.append(basin)

    sizes = []
    for basin in basins:
        sizes.append(len(basin))

    sizes = sorted(sizes)
    print(sizes[-1] * sizes[-2] * sizes[-3])


solve_p2()
