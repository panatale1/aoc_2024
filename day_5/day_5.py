rules = dict()
new_rules = []
updates = []
read_updates = False

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        line = line.strip()
        if not line:
            read_updates = True
            continue
        if read_updates:
            line = line.split(',')
            line = [int(i) for i in line]
            updates.append(line)
        else:
            line = line.split('|')
            line = [int(i) for i in line]
            if line[0] in rules.keys():
                rules[line[0]].append(line[1])
            else:
                rules.update({line[0]: [line[1]]})
            new_rules.append(line)

def check_ordered(data):
    for i in range(len(data)):
        if update[i] not in rules.keys():
            continue
        page_rules = rules[data[i]]
        indexes = [data.index(j) for j in page_rules if j in data]
        indexes = [j for j in indexes if j < i]
        if indexes:
            return False
    return True

def validate_rule(rule, page):
    x, y = rule
    if (x in page and y not in page) or (y in page and x not in page):
        return True
    elif x in page and y in page:
        return page.index(x) == page.index(y)

def order_by_rule(rules, page):
    for rule in rules:
        x, y = rule
        if x in page and y in page:
            if validate_rule(rule, page):
                continue
            else:
                page[page.index(x)] = y
                page[page.index(y)] = x
    return page
 
good_updates = []
bad_updates = []
for update in updates:
    good_updates.append(update) if check_ordered(update) else bad_updates.append(update)
mids = [k[len(k)//2] for k in good_updates]
print(sum(mids))

new_goods = []
for update in bad_updates:
    update = order_by_rule(new_rules, update)
    for rule in new_rules:
        if check_ordered(update):
            continue
        else:
            update = order_by_rule(new_rules, update)
    new_goods.append(update)
print(sum([k[len(k)//2] for k in new_goods]))
