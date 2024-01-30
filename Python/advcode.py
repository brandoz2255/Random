import re

path = "/home/pandulce/char.txt"

with open(path, 'r') as file:
    content = file.read()

lines = content.strip().split('\n')
total_sum = 0

for i, line in enumerate(lines, start=1):
    integers = [int(match) for match in re.findall(r'\d+', line)]
    line_number_sum = int(''.join(map(str, integers)))
    total_sum += line_number_sum
    print(f"Line {i}: Numbers = {line_number_sum}")

print(f"The total sum of all numbers is {total_sum}")



    







