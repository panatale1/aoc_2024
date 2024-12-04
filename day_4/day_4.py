from re import findall

def check_up(i, j):
    up = rows[i][j]
    for k in range(1, 4):
        up += rows[i - k][j]
    return up

def check_down(i, j):
    down = rows[i][j]
    for k in range(1, 4):
        down += rows[i + k][j]
    return down

def check_verticals(i, j):
    up = ''
    down = ''
    if i >= 3:
        up = check_up(i, j)
    if (len(rows) - i) >= 4:
        down = check_down(i, j)
    return [up, down].count('XMAS')

def check_diagonals(i, j):
    ul = rows[i][j]
    ur = rows[i][j]
    dl = rows[i][j]
    dr = rows[i][j]
    if i >= 3 and j >= 3:
        # check up-left
        for k in range(1, 4):
            ul += rows[i - k][j - k]
    if i >= 3 and (len(rows[i]) - j) >= 4:
        # check up-right
        for k in range(1, 4):
            ur += rows[i - k][j + k]
    if (len(rows) - i) >= 4 and j >= 3:
        # check down-left
        for k in range(1, 4):
            dl += rows[i + k][j - k]
    if (len(rows) - i) >= 4 and (len(rows[i]) - j >= 4):
        # check down-right
        for k in range(1, 4):
            dr += rows[i + k][j + k]
    return [ul, ur, dl, dr].count('XMAS')


rows = []
with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        rows.append(line.strip())

total = 0

for i in range(len(rows)):
    total += len(findall('XMAS', rows[i]))
    total += len(findall('SAMX', rows[i]))
    for j in range(len(rows[i])):
        if rows[i][j] != 'X':
            continue
        total += check_verticals(i, j)
        total += check_diagonals(i, j)
print(total)

total = 0
for i in range(len(rows)):
    if i == 0 or i == len(rows) - 1:
        continue
    for j in range(len(rows[i])):
        if j == 0 or j == len(rows[i]) - 1:
            continue
        if rows[i][j] != 'A':
            continue
        corners = [rows[i-1][j-1], rows[i-1][j+1], rows[i+1][j-1], rows[i+1][j+1]]
        if corners.count('M') == 2 and corners.count('S') == 2 and corners[0] != corners[3]:
            total += 1
print(total)
