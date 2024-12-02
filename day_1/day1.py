list_1 = []
list_2 = []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        split_line = line.split()
        list_1.append(int(split_line[0]))
        list_2.append(int(split_line[1]))

list_1.sort()
list_2.sort()

total = 0
for i in range(len(list_1)):
    total += abs(list_2[i] - list_1[i])

print(total)

score = 0
for i in range(len(list_1)):
    score += (list_1[i] * list_2.count(list_1[i]))
print(score)
