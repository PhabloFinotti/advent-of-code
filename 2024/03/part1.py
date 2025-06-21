import re
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')

with open(filePath, 'r') as file:
    lines = file.readlines()


total = 0
for line in lines:
    found = re.findall('mul\\(\\d{1,3},\\d{1,3}\\)', line)
    for multiplication in found:
        numbers = multiplication.replace('mul(', '').replace(')', '').split(',')
        total += int(numbers[0]) * int(numbers[1])
        
print(total)
