# Check safe reports with one error tolerance level
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
file = open(filePath, "r")

all_lines = file.readlines()

arrayOfLines = []
for line in all_lines:
    arrayOfLines.append(list(map(int, line.replace("\n", "").split(" "))))

safeLinesCount = 0
for line in arrayOfLines:
    isSafe = True
    direction = None
    totalItems = len(line)

    for index in reversed(range(totalItems)):
        if index == 0:
            continue
        oldDirection = direction

        if line[index - 1] > line[index]:
            direction = "asc"
        else:
            direction = "desc"

        if oldDirection != None and direction != oldDirection:
            isSafe = False
            break

        numberDistance = abs(line[index - 1] - line[index])
        if numberDistance > 3 or numberDistance < 1:
            isSafe = False
            break

    if isSafe:
        safeLinesCount += 1

print(safeLinesCount)
