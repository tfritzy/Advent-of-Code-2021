import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    input = []
    for line in input_lines:
        input.append(line.strip())
    return input


folder = "Day_10"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())

map = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

reverse_map = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}

point_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def is_corrupt(line):
    stack = []
    for char in line:
        should_break = False
        if (char in map):
            stack.append(char)
        elif(char in reverse_map):
            if (stack[-1] != reverse_map[char]):
                return True
            else:
                stack.pop()
    return False


def solve_p1():
    points = 0
    data = input_data
    for line in data:
        stack = []
        for char in line:
            should_break = False
            if (char in map):
                stack.append(char)
            elif(char in reverse_map):
                if (stack[-1] != reverse_map[char]):
                    points += point_map[char]
                    break
                else:
                    stack.pop()
    print(points)


p2_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def solve_p2():
    data = input_data
    scores = []
    for line in data:
        if (is_corrupt(line)):
            continue

        stack = []
        full_line = line
        for char in line:
            should_break = False
            if (char in map):
                stack.append(char)
            elif(char in reverse_map):
                stack.pop()

        score = 0
        while (len(stack) > 0):
            score *= 5
            score += p2_score_map[map[stack.pop()]]
        scores.append(score)
    print(sorted(scores)[int(len(scores) // 2)])


solve_p2()
