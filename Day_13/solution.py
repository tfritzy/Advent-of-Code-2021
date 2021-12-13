import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    grid = []
    size_x = 0
    size_y = 0
    for line in input_lines:
        if (line == "\n"):
            break

        splits = line.strip().split(",")
        x = int(splits[0]) + 1
        y = int(splits[1]) + 1
        if (y > size_y):
            size_y = y
        if (x > size_x):
            size_x = x

    grid = []
    for y in range(size_y):
        grid.append(["."] * size_x)

    is_getting_folds = False
    folds = []
    for line in input_lines:
        if (line == "\n"):
            is_getting_folds = True
            continue

        if (not is_getting_folds):
            splits = line.strip().split(",")
            x = int(splits[0])
            y = int(splits[1])
        else:
            splits = line.strip().split('=')
            folds.append([splits[0], int(splits[1])])

        grid[y][x] = "#"

    return (grid, folds)


folder = "Day_13"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def print_grid(grid):
    for line in grid:
        print("".join(line))


def solve():
    (grid, folds) = input_data

    for fold in folds:
        index = fold[1]
        is_x = "x" in fold[0]

        if (is_x):
            other_side = index - 1
            for x in range(index + 1, len(grid[0])):
                if (other_side < 0):
                    break
                for y in range(len(grid)):
                    if (grid[y][x] == "#"):
                        grid[y][other_side] = "#"
                other_side -= 1
            for i in range(len(grid)):
                grid[i] = grid[i][0:index]
        else:
            other_side = index - 1
            for y in range(index + 1, len(grid)):
                if (other_side < 0):
                    break
                for x in range(len(grid[0])):
                    if (grid[y][x] == "#"):
                        grid[other_side][x] = "#"
                other_side -= 1
            grid = grid[0:index]

    dot_count = 0
    for line in grid:
        dot_count += line.count("#")

    print_grid(grid)
    print(folds)
    print(dot_count)


solve()
