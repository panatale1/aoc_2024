import fileinput
from pprint import pprint

lab_map = []
fresh_map = []
i = 0
filename = 'input.txt'
with open(filename, 'r') as infile:
    for line in infile.readlines():
        line = line.strip()
        if '^' in line:
            origin = [i, line.index('^')]
        line = [x for x in line]
        lab_map.append(line)
        fresh_map.append(line)
        i += 1
start = origin

def check_for_obstacle(origin, direction):
    if direction == 'UP':
        forward = [origin[0] - 1, origin[1]]
    elif direction == 'RIGHT':
        forward = [origin[0], origin[1] + 1]
    elif direction == 'DOWN':
        forward = [origin[0] + 1, origin[1]]
    else:
        forward = [origin[0], origin[1] - 1]
    if lab_map[forward[0]][forward[1]] == '#':
        return True
    return False

def check_guard_leaves(origin, direction):
    if direction == 'UP' and origin[0] == 0:
        return True
    elif direction == 'LEFT' and origin[1] == 0:
        return True
    elif direction == 'DOWN' and origin[0] == len(lab_map) - 1:
        return True
    elif direction == 'RIGHT' and origin[1] == len(lab_map[0]) - 1:
        return True
    return False

directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
turns = 0
guard_leaves = False
while not guard_leaves:
    direction = directions[turns % 4]
    # check in front of guard
    if check_guard_leaves(origin, direction):
        break
    if check_for_obstacle(origin, direction):
        turns += 1
        continue

    lab_map[origin[0]][origin[1]] = 'X'
    if direction == 'UP':
        origin[0] -= 1
    elif direction == 'RIGHT':
        origin[1] += 1
    elif direction == 'DOWN':
        origin[0] += 1
    elif direction == 'LEFT':
        origin[1] -= 1

locations = [row.count('X') for row in lab_map]
print(sum(locations) + 1)

g = {(x, y): c for y, r in enumerate(fileinput.input(filename)) for x, c in enumerate(r.strip('\n'))}
w,h = max((x + 1, y + 1) for x,y, in g.keys())
s = min(k for k, v in g.items() if v == '^')

p, d, c = s, 0, set()
while p in g:
    c.add(p)
    n = (p[0] + (0, 1, 0, -1)[d], p[1] + (-1, 0, 1, 0)[d])
    if g.get(n) == '#':
        d = (d + 1) % 4
    else:
        p = n

j = {}
for y in range(h):
    l = ((-1, y), 0)
    for x in range(w):
        if g.get((x,y)) == '#':
            l = ((x+1, y), 0)
        j[(x,y,3)] = l
    l = ((w,y), 2)
    for x in range(w-1, -1, -1):
        if g.get((x,y)) == '#':
            l = ((x-1,y),2)
        j[(x,y,1)] = l
for x in range(w):
    l = ((x, -1), 1)
    for y in range(h):
        if g.get((x,y)) == '#':
            l = ((x,y+1),1)
        j[(x,y,0)] = l
    l = ((x,h),3)
    for y in range(h - 1, -1, -1):
        if g.get((x,y)) == '#':
            l = ((x,y-1),3)
        j[(x,y,2)] = l
t = 0
for o in c:
    if g[o] != '.':
        continue
    p, d, v = s, 0, set()
    while p in g and (p, d) not in v:
        v.add((p,d))
        if p[0] != o[0] and p[1] != o[1]:
            p, d = j[(*p, d)]
        else:
            n = (p[0] + (0, 1, 0, -1)[d], p[1] + (-1,0,1,0)[d])
            if g.get(n) == '#' or n == o:
                d = (d + 1) % 4
            else:
                p = n
    t += (p,d) in v
print(t)
