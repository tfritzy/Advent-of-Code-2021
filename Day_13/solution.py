import copy
import math
from os import truncate
from typing import NewType


def parse_input(input_lines):
    template = input_lines[0].strip()
    rules = []
    for i in range(2, len(input_lines)):
        line = input_lines[i]
        rules.append(line.strip().split(" -> "))
    return (template, rules)


folder = "Day_14"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def get_pairs(poly):
    pairs = {}
    for i in range(1, len(poly)):
        pair = poly[i - 1] + poly[i]
        if (pair not in pairs):
            pairs[pair] = 0
        pairs[pair] += 1
    return pairs


def get_element_comonalities(pairs):
    counts = {}
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        if (first not in counts):
            counts[first] = 0
        if (second not in counts):
            counts[second] = 0
        counts[first] += pairs[pair]
        counts[second] += pairs[pair]

    for letter in counts:
        counts[letter] /= 2

    return sorted(counts.values())


def solve():
    template, rules = input_data
    pairs = get_pairs(template)
    for i in range(40):
        print(pairs)
        print(sum(get_element_comonalities(pairs)))
        print(get_element_comonalities(pairs))
        new_pairs = pairs.copy()
        for rule in rules:
            if (rule[0] in pairs):
                new_pair_1 = rule[0][0] + rule[1]
                new_pair_2 = rule[1] + rule[0][1]
                if (new_pair_1 not in new_pairs):
                    new_pairs[new_pair_1] = 0
                if (new_pair_2 not in new_pairs):
                    new_pairs[new_pair_2] = 0
                new_pairs[new_pair_1] += pairs[rule[0]]
                new_pairs[new_pair_2] += pairs[rule[0]]
                new_pairs[rule[0]] -= pairs[rule[0]]
        pairs = new_pairs

    commons = get_element_comonalities(pairs)
    print(commons[-1] - commons[0])


solve()
