# Calculate the similarity score
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
file = open(filePath, 'r')

all_lines = file.readlines()

numberlist1 = []
numberlist2 = []
for line in all_lines:
  splitted = line.replace('\n', '').split(' ')
  numberlist1.append(int(splitted[0]))
  numberlist2.append(int(splitted[3]))

repetitionMap = dict()
for index, number in enumerate(numberlist1):
  if number not in repetitionMap:
    repetitionMap[number] = 0

for number in numberlist2:  
  if number in repetitionMap:
    repetitionMap[number] = int(repetitionMap[number]) + 1

similaritySum = 0
for item in repetitionMap:
  similaritySum += item * repetitionMap[item]

print(similaritySum)
