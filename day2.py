file = open("./inputs/day2.txt", "r")
lines = file.readlines()
file.close()

points = { "X": 1, "Y": 2, "Z": 3 }
conditions = {
    "A": {
        "X": [ "Z", 0 ],
        "Y": [ "X", 3 ],
        "Z": [ "Y", 6 ],
    },
    "B": {
        "X": [ "X", 0 ],
        "Y": [ "Y", 3 ],
        "Z": [ "Z", 6 ],
    },
    "C": {
        "X": [ "Y", 0 ],
        "Y": [ "Z", 3 ],
        "Z": [ "X", 6 ],
    }
}

score = 0;
for line in lines:
    p1move = line.replace("\n", "").split()[0]
    roundEnd = line.replace("\n", "").split()[1]

    winCondition = conditions[p1move][roundEnd]   
    score += points[winCondition[0]]
    score += winCondition[1]

print(score)