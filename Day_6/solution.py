import copy
import math
from typing import NewType


def parse_input(input_lines):
    input = input_lines[0].split(",")
    for i in range(len(input)):
        input[i] = int(input[i])
    return input


folder = "Day_6"
part1_data = parse_input(open(f"{folder}/Part1Data.txt").readlines())
part2_data = parse_input(open(f"{folder}/Part2Data.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())

print(test_data)


def solve():
    data = part1_data

    fish_timer_counts = [0] * 9
    for num in data:
        fish_timer_counts[num] += 1

    for day in range(256):
        num_new = fish_timer_counts.pop(0)
        fish_timer_counts.append(num_new)
        fish_timer_counts[6] += num_new
        print(fish_timer_counts)

    print(sum(fish_timer_counts))


solve()
