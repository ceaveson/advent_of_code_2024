with open("input.txt") as f:
    reports = [report.strip() for report in f.readlines()]


def safety_evaluation(report):
    report_items = [int(item) for item in report.split()]
    last_item = report_items[0]

    # figure out if reports should keep increasing or decreaseing in value
    if report_items[1] > report_items[0]:
        increasing = True
    elif report_items[1] < report_items[0]:
        increasing = False
    else:
        return False

    # Check if report values keep increasing or decreasing or same as last value
    for item in report_items[1:]:
        if item == last_item:
            return False
        if increasing:
            if item < last_item:
                return False
        else:
            if item > last_item:
                return False
        
        # Check if item and last_item are more than 3 numbers apart
        if increasing:
            if len(range(item, last_item, -1)) > 3:
                return False
        else:
            if len(range(item, last_item)) > 3:
                return False

        last_item = item
    return True


safe_reports = 0

for report in reports:
    if safety_evaluation(report):
        safe_reports += 1

print(safe_reports)
