with open("input.txt") as f:
    inputs = f.readlines()

list_a = [input.split()[0] for input in inputs]
list_b = [input.split()[1] for input in inputs]


def similarity_score(num, list_to_check):
    count = 0
    for i in list_to_check:
        if i == num:
            count += 1
    score = int(num) * count
    return score


total = 0


for num in list_a:
    total += similarity_score(num, list_b)

print(total)
