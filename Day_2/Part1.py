folder = "Day_2"


def part_one():
    data = open(f"{folder}/Part1Data.txt").readlines()
    # data = open(f"{folder}/Test.txt").readlines()
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        data[i][1] = int(data[i][1])
    print(data)

    horizontal = 0
    depth = 0
    aim = 0
    for command in data:
        if (command[0] == "forward"):
            horizontal += command[1]
            depth += aim * command[1]
        elif(command[0] == "up"):
            aim -= command[1]
        elif(command[0] == "down"):
            aim += command[1]
    print(horizontal * depth)


def part_two():
    data = open(f"{folder}/Part2Data.txt").readlines()
    for i in range(len(data)):
        data[i] = int(data[i].strip())


part_one()
