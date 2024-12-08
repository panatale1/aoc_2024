from datetime import datetime
from math import prod
calibrations = []
with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        line = line.strip().split(':')
        val, line = int(line[0]), line[1]
        line = [int(x) for x in line.strip().split()]
        line.insert(0, val)
        calibrations.append(line)

class CalibrationTree():
    def __init__(self, pair):
        self.pair = pair
        self.sum = None
        self.prod = None
        self.concat = None

    def add_children(self, number):
        self.sum = CalibrationTree([sum(self.pair), number])
        self.prod = CalibrationTree([prod(self.pair), number])
        self.concat = CalibrationTree([int(str(self.pair[0]) + str(self.pair[1])), number])

def add_nodes(node, number):
    if node.sum is None:
        # no children
        node.add_children(number)
        return
    add_nodes(node.sum, number)
    add_nodes(node.prod, number)
    add_nodes(node.concat, number)

def get_totals(node, total_list):
    if node.sum is None:
        total_list.append(sum(node.pair))
        total_list.append(prod(node.pair))
        total_list.append(int(str(node.pair[0]) + str(node.pair[1])))
        return total_list
    total_list = get_totals(node.sum, total_list)
    total_list = get_totals(node.prod, total_list)
    total_list = get_totals(node.concat, total_list)
    return total_list

start = datetime.now()
good_vals = []
for line in calibrations:
    result = line.pop(0)
    if len(line) == 2:
        # only two values, no need for the tree approach
        if sum(line) == result or prod(line) == result or int(str(line[0]) + str(line[1])) == result:
            good_vals.append(result)
    else:
        root = CalibrationTree(line[:2])
        line = line[2:]
        for num in line:
            add_nodes(root, num)
        total_list = get_totals(root, [])
        if result in total_list:
            good_vals.append(result)
end = datetime.now()
print(sum(good_vals))
print(end - start)
