lines = open("./inputs/day3.txt").readlines()

def getPriority(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96

groups = []
current_group = []
count = 0
for line in lines:
    current_group.append(line.replace("\n", ""))
    count += 1

    if count == 3:
        groups.append(current_group)
        current_group = []
        count = 0    

total = 0
for group in groups:
    common_letter = ""
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                common_letter = letter
                break

    total += getPriority(common_letter)


print(total)