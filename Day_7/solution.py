import copy
import math
from typing import NewType


def parse_input(input_lines):
    input = input_lines[0].split(",")
    for i in range(len(input)):
        input[i] = int(input[i])
    return input


folder = "Day_7"
part1_data = parse_input(open(f"{folder}/Part1Data.txt").readlines())
part2_data = parse_input(open(f"{folder}/Part2Data.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def get_fuel_cost(orientation, num: int):
    cost = 0
    for pos in orientation:
        cost += abs(pos - num)
    return cost


def get_fuel_cost_p2(orientation, num: int):
    cost = 0
    for pos in orientation:
        diff = abs(pos - num)
        cost += diff * ((1 + diff) / 2)
    return cost


def solve():
    data = part1_data
    low = 0
    high = max(data)
    while (True):
        cur_cost = get_fuel_cost_p2(data, low + (high - low) // 2)
        upper_bucket_cost = get_fuel_cost_p2(data, low + (high - low) // 2 + 1)
        lower_bucket_cost = get_fuel_cost_p2(data, low + (high - low) // 2 - 1)
        if (upper_bucket_cost < cur_cost):
            low = low + (high - low) // 2
        elif (lower_bucket_cost < cur_cost):
            high = low + (high - low) // 2
        else:
            print(cur_cost)
            return
        print(cur_cost)


solve()
