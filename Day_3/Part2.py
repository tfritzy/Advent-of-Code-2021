data = open("Part2Data.txt").readlines()
for i in range(len(data)):
    data[i] = int(data[i].strip())

window = []
lastest_sum = 100000
count = 0
for number in data:
    window.append(number)
    if (len(window) > 3):
        window.pop(0)
    if (len(window) == 3):
        if (sum(window) > lastest_sum):
            count += 1
        lastest_sum = sum(window)

print(count)
