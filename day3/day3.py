import re

with open("day3/input.txt", "r") as f:
    data = f.read()
sum = 0
regex = "mul\(\d+,\d+\)"

def mul(a,b):
    return a*b

x = re.findall(regex, data)
for i in x:
    a,b = map(int, re.findall("\d+", i))
    sum += mul(a,b)

print(sum)