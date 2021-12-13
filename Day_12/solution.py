import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    graph = {}
    for line in input_lines:
        splits = line.strip().split("-")

        start = splits[0]
        end = splits[1]
        if (start not in graph):
            graph[start] = []
        graph[start].append(end)

        if (end not in graph):
            graph[end] = []
        graph[end].append(start)
    return graph


folder = "Day_12"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def explore(path, graph, double_small):
    paths = []
    possible_next = graph[path[-1]]

    if (path[-1] == "end"):
        paths.append(path)
        return paths

    for option in possible_next:
        is_big = option.isupper()
        if (is_big):
            new_path = path.copy()
            new_path.append(option)
            paths.extend(explore(new_path, graph, double_small))
        elif (option != "start"):
            if (option not in path):
                new_path = path.copy()
                new_path.append(option)
                paths.extend(explore(new_path, graph, double_small))
            elif (double_small == "" and option != "end"):
                new_path = path.copy()
                new_path.append(option)
                paths.extend(explore(new_path, graph, option))

    return paths


def solve():
    data = input_data
    paths = explore(["start"], data, "")
    print(paths)
    print(len(paths))


solve()
