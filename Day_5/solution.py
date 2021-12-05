import copy
import math


def parse_input(input_lines):
    lines = []
    for line in input_lines:
        points = line.split(" -> ")
        start = points[0].split(",")
        start = [int(start[0]), int(start[1])]
        end = points[1].split(",")
        end = [int(end[0]), int(end[1])]
        lines.append((start, end))
    return lines


folder = "Day_5"
part1_data = parse_input(open(f"{folder}/Part1Data.txt").readlines())
part2_data = parse_input(open(f"{folder}/Part2Data.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())

print(test_data)


def solve():
    data = part1_data
    point_counts = {}
    for line in data:
        y_step = 0
        if (line[1][1] != line[0][1]):
            y_step = -1 if line[1][1] < line[0][1] else 1
        x_step = 0
        if (line[1][0] != line[0][0]):
            x_step = -1 if line[1][0] < line[0][0] else 1
        iter = [line[0][0], line[0][1]]

        key = f"{iter[0]},{iter[1]}"
        if (key not in point_counts):
            point_counts[key] = 0
        point_counts[key] += 1
        while(iter != line[1]):
            iter[0] += x_step
            iter[1] += y_step
            key = f"{iter[0]},{iter[1]}"
            if (key not in point_counts):
                point_counts[key] = 0
            point_counts[key] += 1

        # for y in range(line[0][1], line[1][1] + y_step, y_step):
        #     for x in range(line[0][0], line[1][0] + x_step, x_step):
        #         key = f"{x},{y}"
        #         if (key not in point_counts):
        #             point_counts[key] = 0
        #         point_counts[key] += 1

    num_overlap = 0
    for key, value in point_counts.items():
        if (value > 1):
            num_overlap += 1
    print(num_overlap)


solve()
