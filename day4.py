lines = open("./inputs/day4.txt").readlines()

total = 0
for line in lines:
    ranges = line.split(",")

    first = ranges[0].split("-")
    second = ranges[1].split("-")
    mins_and_maxs = [ [ int(first[0]), int(first[1]) ], [ int(second[0]), int(second[1]) ] ]

    if mins_and_maxs[0][0] >= mins_and_maxs[1][0] and mins_and_maxs[0][0] <= mins_and_maxs[1][1]:
        total += 1
    elif mins_and_maxs[0][1] >= mins_and_maxs[1][0] and mins_and_maxs[0][1] <= mins_and_maxs[1][1]:
        total += 1
    elif mins_and_maxs[1][0] >= mins_and_maxs[0][0] and mins_and_maxs[1][0] <= mins_and_maxs[0][1]:
        total += 1
    elif mins_and_maxs[1][1] >= mins_and_maxs[0][0] and mins_and_maxs[1][1] <= mins_and_maxs[0][1]:
        total += 1

print(total)