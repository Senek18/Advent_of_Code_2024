import re

with open("day13/input.txt", "r") as f:
    data = f.read().splitlines()

def has_decimal(number):
    return not number.is_integer()

add = 10000000000000
# add = ""

count = 0
for idx, i in enumerate(range(0, len(data), 4)):
    match = re.search(r"X\+([0-9]+).*?Y\+([0-9]+)", data[i])
    l1 = int(match.group(1))
    l3 = int(match.group(2))
    match = re.search(r"X\+([0-9]+).*?Y\+([0-9]+)", data[i+1])
    l2 = int(match.group(1))
    l4 = int(match.group(2))
    match = re.search(r"X=([0-9]+),.*?Y=([0-9]+)", data[i+2])
    c1 = int(match.group(1)) + add 
    c2 = int(match.group(2)) + add
    b = (c1*l3 - c2*l1) / (l2*l3 - l1*l4)
    a = (c1 - b*l2) / l1
    if has_decimal(a) or has_decimal(b):
        continue
    count += a*3+b
    print(idx, a ,b)
print(count)