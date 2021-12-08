import copy
import math
from typing import NewType


def parse_input(input_lines):
    input = []
    for line in input_lines:
        parts = line.strip().split(" | ")
        signals = parts[0].split(" ")
        output = parts[1].split(" ")
        input.append([signals, output])
    return input


folder = "Day_8"
part1_data = parse_input(open(f"{folder}/Part1Data.txt").readlines())
part2_data = parse_input(open(f"{folder}/Part2Data.txt").readlines())
test_data = parse_input(open(f"{folder}/Test.txt").readlines())


def convert_code_to_digit(code):
    sorted_code = "".join(sorted(code))
    if (sorted_code == "abcefg"):
        return 0
    elif(sorted_code == "cf"):
        return 1
    elif(sorted_code == "acdeg"):
        return 2
    elif(sorted_code == "acdfg"):
        return 3
    elif(sorted_code == "bcdf"):
        return 4
    elif(sorted_code == "abdfg"):
        return 5
    elif(sorted_code == "abdefg"):
        return 6
    elif(sorted_code == "acf"):
        return 7
    elif(sorted_code == "abcdfg"):
        return 9
    else:
        return 8


def solve():
    data = part1_data
    num_digits = 0
    total = 0
    for input in data:
        digit_possibilites = {
            'a': set('abcdefg'),
            'b': set('abcdefg'),
            'c': set('abcdefg'),
            'd': set('abcdefg'),
            'e': set('abcdefg'),
            'f': set('abcdefg'),
            'g': set('abcdefg')}
        unparsed_codes = []
        for code in input[0]:
            if (len(code) == 2):
                for char in code:
                    digit_possibilites[char] = digit_possibilites[char].intersection(
                        set("cf"))
                for key in digit_possibilites:
                    if (key not in code):
                        digit_possibilites[key].discard("c")
                        digit_possibilites[key].discard("f")
            elif (len(code) == 3):
                for char in code:
                    digit_possibilites[char] = digit_possibilites[char].intersection(
                        set("acf"))
                for key in digit_possibilites:
                    if (key not in code):
                        digit_possibilites[key].discard("a")
                        digit_possibilites[key].discard("c")
                        digit_possibilites[key].discard("f")
            elif (len(code) == 4):
                for char in code:
                    digit_possibilites[char] = digit_possibilites[char].intersection(
                        set("bcdf"))
                for key in digit_possibilites:
                    if (key not in code):
                        digit_possibilites[key].discard("b")
                        digit_possibilites[key].discard("c")
                        digit_possibilites[key].discard("d")
                        digit_possibilites[key].discard("f")
            else:
                unparsed_codes.append(code)

        code_counts = {}
        for code in unparsed_codes:
            code_len = len(code)
            if (code_len not in code_counts):
                code_counts[code_len] = []
            code_counts[code_len].append(code)

        char_counts_6 = {}
        for code in code_counts[6]:
            for char in code:
                if (char not in char_counts_6):
                    char_counts_6[char] = 0
                char_counts_6[char] += 1

        chars_for_6_len = set()
        for char in char_counts_6:
            if (char_counts_6[char] == 2):
                chars_for_6_len.add(char)

        for char in chars_for_6_len:
            # must be d, c, or e
            for key in digit_possibilites:
                if (key not in chars_for_6_len):
                    digit_possibilites[key].discard("d")
                    digit_possibilites[key].discard("c")
                    digit_possibilites[key].discard("e")
                else:
                    digit_possibilites[key] = digit_possibilites[key].intersection(
                        set("dce"))

                    # if (len(code) == 6):
                    #     # could be 0, 6, or 9
        print(digit_possibilites)

        translation_map = {}
        for key in digit_possibilites:
            source = list(digit_possibilites[key])[0]
            translation_map[key] = source

        digits = ""
        for code in input[1]:
            actual_code = ""
            for char in code:
                actual_code += translation_map[char]
            digits += str(convert_code_to_digit(actual_code))
        total += int(digits)

    print(total)


solve()
