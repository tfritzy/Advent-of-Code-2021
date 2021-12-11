import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    input = []
    for line in input_lines:
        nums = []
        for char in line.strip():
            nums.append(int(char))
        input.append(nums)
    return input


folder = "Day_11"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def inc_neighbors(x, y, data):
    for y in range(y-1, y + 2):
        if (y < 0 or y > len(data)):
            continue
        for x in range(x - 1, x + 2):
            if (x < 0 or x > len(data[0])):
                continue
            data[y][x] += 1


def increment_oct(x, y, data, has_flashed):
    data[y][x] += 1
    if (data[y][x] > 9 and (x, y) not in has_flashed):
        has_flashed.add((x, y))
        for y_i in range(y-1, y + 2):
            if (y_i < 0 or y_i >= len(data)):
                continue
            for x_i in range(x - 1, x + 2):
                if (x_i < 0 or x_i >= len(data[0])):
                    continue
                increment_oct(x_i, y_i, data, has_flashed)


def solve():
    data = input_data
    num_flashes = 0
    for i in range(100000):
        has_flashed = set()
        for y in range(len(data)):
            for x in range(len(data)):
                increment_oct(x, y, data, has_flashed)
        num_flashes += len(has_flashed)
        for flasher in has_flashed:
            data[flasher[1]][flasher[0]] = 0

        if (len(has_flashed) == len(data) * len(data[0])):
            print("Synced")
            print(i)
            return
    print(num_flashes)


solve()
