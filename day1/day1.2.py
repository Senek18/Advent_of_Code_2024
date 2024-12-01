left_list = []
right_list = []

with open('day1\input.txt', 'r') as fh:
    for line in fh:
        l, r = line.split("   ")
        left_list.append(int(l))
        right_list.append(int(r))

sum = 0
for value in left_list:
    sum += (value * right_list.count(value))

print(sum)
