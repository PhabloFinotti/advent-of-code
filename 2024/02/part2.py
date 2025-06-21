# Check safe reports with one error tolerance level
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
file = open(filePath, "r")

all_lines = file.readlines()

arrayOfLines = []
for line in all_lines:
    arrayOfLines.append(list(map(int, line.replace("\n", "").split(" "))))


def isLineSafe(line):
    direction = None
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if diff != 0:
            direction = "asc" if diff > 0 else "desc"
            break

    if direction is None:
        return False

    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if direction == "asc" and diff <= 0:
            return False
        if direction == "desc" and diff >= 0:
            return False

    return True


safeLinesCount = 0
for line in arrayOfLines:
    isSafe = True

    isSafe = isLineSafe(line)

    if isSafe == False:
        for i in range(len(line)):
            new_line = line[:i] + line[i + 1 :]
            if isLineSafe(new_line):
                isSafe = True
                break

    if isSafe:
        safeLinesCount += 1

print(safeLinesCount)
