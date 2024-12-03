from copy import deepcopy
from re import findall


def do_muls(instruction_string):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    muls = findall(pattern, instruction_string)
    nums = []
    for mul in muls:
        nums.append(findall(r'\d{1,3},\d{1,3}', mul)[0])
    total = 0
    for pair in nums:
        n1, n2 = pair.split(',')
        total += (int(n1) * int(n2))
    return total

lines = ''

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        lines += line.strip()

print(do_muls(lines))

instructions = deepcopy(lines)
dos = ''
while len(instructions) > 0:
    try:
        split_instructions = instructions.split("don't()", maxsplit=1)
        instructions = split_instructions[1]
        dos += split_instructions[0]
        split_instructions = instructions.split("do()", maxsplit=1)
        instructions = split_instructions[1]
    except IndexError:
        instructions = []
print(do_muls(dos))
