import re

with open("day3/input.txt", "r") as f:
    data = f.read()

sum = 0
regex = "mul\(\d+,\d+\)|don'?t\(\)|do\(\)"

def mul(a,b):
    return a*b

x = re.findall(regex, data)

mul_bool = True

for i in x:
    if i == "don't()":
        mul_bool = False
    elif i == "do()":
        mul_bool = True
    else:
        if mul_bool:
            a,b = map(int, re.findall("\d+", i))
            sum += mul(a,b)

print(sum)