from bitstring import BitArray

folder = "Day_3"

part1_data = open(f"{folder}/Part1Data.txt").readlines()
part2_data = open(f"{folder}/Part2Data.txt").readlines()
test_data = open(f"{folder}/Test.txt").readlines()


def part_one():
    data = part1_data
    one_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in data:
        num = num.strip()
        for i in range(len(num)):
            if (num[i] == '0'):
                zero_counts[i] += 1
            else:
                one_counts[i] += 1

    gamma = ""
    epsilon = ""
    for i in range(len(one_counts)):
        if (one_counts[i] > zero_counts[i]):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(f"Gamma: {int(gamma, 2)}")
    print(f"Epsilon: {int(epsilon, 2)}")

    print(int(gamma, 2) * int(epsilon, 2))


def part_two():
    oxygen_numbers = set()
    scrubber_numbers = set()
    for number in part1_data:
        oxygen_numbers.add(number.strip())
        scrubber_numbers.add(number.strip())

    for i in range(len(part1_data[0].strip())):
        most_common = most_common_digit(oxygen_numbers, i)
        least_common = "1" if most_common_digit(
            scrubber_numbers, i) == "0" else "0"

        if (len(oxygen_numbers) > 1):
            remaining_oxygen = set()
            for number in oxygen_numbers:
                if (number[i] == most_common):
                    remaining_oxygen.add(number)
            oxygen_numbers = remaining_oxygen

        if (len(scrubber_numbers) > 1):
            remaining_scrubber = set()
            for number in scrubber_numbers:
                if (number[i] == least_common):
                    remaining_scrubber.add(number)
            scrubber_numbers = remaining_scrubber

    print(int(list(oxygen_numbers)[0], 2) * int(list(scrubber_numbers)[0], 2))


def most_common_digit(numbers, position):
    zeroCount = 0
    for number in numbers:
        if (number[position] == "0"):
            zeroCount += 1
        else:
            zeroCount -= 1
    return "0" if zeroCount > 0 else "1"


part_two()
