left_list = []
right_list = []

with open('day1\input.txt', 'r') as fh:
    for line in fh:
        l, r = line.split("   ")
        left_list.append(int(l))
        right_list.append(int(r))

left_list.sort()
right_list.sort()

sum = 0
for x,y in zip(left_list, right_list):
    sum += abs(y - x)

print(sum)