with open("input.txt") as f:
    inputs = f.readlines()

list_a = [input.split()[0] for input in inputs]
list_b = [input.split()[1] for input in inputs]
distances = []

list_a.sort()
list_b.sort()

for i in range(0, len(list_a)):
    nums = [int(list_a[i]), int(list_b[i])]
    nums.sort()
    distances.append(nums[1] - nums[0])

total = 0
for i in distances:
    total += i

print(total)
