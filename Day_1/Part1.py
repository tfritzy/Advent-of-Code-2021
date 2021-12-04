data = open("Part1Data.txt").readlines()
for i in range(len(data)):
    data[i] = int(data[i].strip())

count = 0
last = data[0]
for i in range(1, len(data)):
    num = data[i]
    if (num > last):
        count += 1
    last = num

print(count)
