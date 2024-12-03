from copy import deepcopy

def test_ordered(report):
    sort_report = deepcopy(report)
    sort_report.sort()
    if report == sort_report:
        return True
    sort_report.sort(reverse=True)
    if report == sort_report:
        return True
    return False

def problem_dampener(report):
    for i in range(len(report)):
        new_report = report[0:i] + report[i+1:]
        if test_ordered(new_report):
            for j in range(len(new_report) - 1):
                if abs(new_report[j] - new_report[j + 1]) > 3 or new_report[j] == new_report[j + 1]:
                    break
            else:
                return True
    return False
            
reports = []
good_reports = []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        reports.append(line.split())

for i in range(len(reports)):
    for j in range(len(reports[i])):
        reports[i][j] = int(reports[i][j])

reports_len = len(reports)
print(reports_len)
j = 0
while j < reports_len:
    if test_ordered(reports[j]):
        for i in range(len(reports[j]) - 1):
            if abs(int(reports[j][i]) - int(reports[j][i + 1])) > 3 or int(reports[j][i]) - int(reports[j][i + 1]) == 0:
                j += 1
                break
        else:
            good_reports.append(reports[j]) 
            reports.pop(j)
            reports_len -= 1
    else:
        j += 1
print(len(good_reports))

for report in reports:
    if problem_dampener(report):
        good_reports.append(report)

print(len(good_reports))
