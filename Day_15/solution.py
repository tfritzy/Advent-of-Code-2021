from copy import copy, deepcopy
import math
from os import truncate
from typing import NewType
import queue


def parse_input(input_lines):
    grid = []
    for line in input_lines:
        line = line.strip()
        nums = []
        for num in line:
            nums.append(int(num))
        grid.append(nums)
    return grid


folder = "Day_15"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def in_bounds(grid, x, y):
    if (x < 0 or x >= len(grid[0])):
        return False
    if (y < 0 or y >= len(grid)):
        return False
    return True


def explore(grid, costs):
    q = []
    q.append((0, 0, 0))
    counter = 0
    while (len(q) > 0):
        if (counter % 100000 == 0):
            print(len(q))
        counter += 1

        min_dist = q[0][2]
        min_index = 0
        for i in range(len(q)):
            item = q[i]
            if (item[2] < min_dist):
                min_dist = item[2]
                min_index = i

        cur = q.pop(min_index)
        x = cur[0]
        y = cur[1]
        cost = cur[2]

        if (in_bounds(grid, x + 1, y)):
            new_cost = cost + grid[y][x+1]
            if (costs[y][x + 1] > new_cost):
                costs[y][x + 1] = new_cost
                q.append((x + 1, y, new_cost))

        if (in_bounds(grid, x - 1, y)):
            new_cost = cost + grid[y][x-1]
            if(costs[y][x - 1] > new_cost):
                costs[y][x - 1] = new_cost
                q.append((x - 1, y, new_cost))

        if (in_bounds(grid, x, y + 1)):
            new_cost = cost + grid[y+1][x]
            if (costs[y + 1][x] > new_cost):
                costs[y + 1][x] = new_cost
                q.append((x, y + 1, new_cost))

        if (in_bounds(grid, x, y - 1)):
            new_cost = cost + grid[y-1][x]
            if (costs[y - 1][x] > new_cost):
                costs[y - 1][x] = new_cost
                q.append((x, y - 1, new_cost))


def solve():
    data = input_data

    for line in data:
        new_line = line.copy()
        for i in range(4):
            for i in range(len(new_line)):
                new_line[i] += 1
                if (new_line[i] > 9):
                    new_line[i] = 1
            line.extend(new_line)

    first_block = deepcopy(data)
    for i in range(4):
        first_block = deepcopy(first_block)
        for y in range(len(first_block)):
            for x in range(len(first_block[0])):
                first_block[y][x] += 1
                if first_block[y][x] > 9:
                    first_block[y][x] = 1
        data.extend(first_block)

    costs = []
    for i in range(len(data)):
        costs.append([100000000] * len(data[0]))

    print(test_data)
    explore(data, costs)
    print(costs)
    print(costs[len(costs) - 1][len(costs[0]) - 1])


solve()
