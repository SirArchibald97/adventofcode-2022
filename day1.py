file = open("./inputs/day1.txt", "r")
lines = file.readlines()
file.close()

localTotal = 0
totals = []
for line in lines:
    if (line != "\n"):
        localTotal += int(line.replace("\n", ""))
        print(int(line.replace("\n", "")))
    else:
        print("new line")
        totals.append(localTotal)
        localTotal = 0

highestTotals = []
while len(highestTotals) != 3:
    currentHighest = 0
    for total in totals:
        if total > currentHighest and total not in highestTotals:
            currentHighest = total
    highestTotals.append(currentHighest)

print(sum(highestTotals))