import re
import os

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')

with open(filePath, 'r') as file:
    content = file.read()

total = 0
lastMulPos = 0
for mulFound in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', content):
    mul = mulFound.group(0)
    pos = mulFound.start()
    textBefore = content[:pos]

    lastFound = re.findall(r"don't|do", textBefore)
    if len(lastFound) > 0 and lastFound[-1] == "don't":
        continue

    numbers = mul.replace('mul(', '').replace(')', '').split(',')
    total += int(numbers[0]) * int(numbers[1])
        
print(total)
