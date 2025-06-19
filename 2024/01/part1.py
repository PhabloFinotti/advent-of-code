# Calculate the difference between values
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
file = open(filePath, 'r')

all_lines = file.readlines()

numberSet1 = []
numberSet2 = []
for line in all_lines:
  splitted = line.replace('\n', '').split(' ')
  numberSet1.append(int(splitted[0]))
  numberSet2.append(int(splitted[3]))

sortedNumbers1 = sorted(numberSet1)
sortedNumbers2 = sorted(numberSet2)

result = 0
for index in range(len(sortedNumbers1)):
  result += abs(sortedNumbers1[index] - sortedNumbers2[index])

print(result) # 936063
