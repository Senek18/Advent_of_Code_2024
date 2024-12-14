import re

with open("day14/input.txt", "r") as f:
    data = f.read().splitlines()

wide = 101
tall = 103
matrix = [[0 for _ in range(wide)] for _ in range(tall)]

def check_boundary(p):
    row = p[1]
    col = p[0]
    if row < 0:
        row = tall + row
    elif row >= tall:
        row = row - tall
    
    if col < 0:
        col = wide + col
    elif col >= wide:
        col = col - wide

    return (col, row)

for line in data:
    p, v = re.findall(r"-?\d+,-?\d+", line)
    p = list(map(int, p.split(",")))
    v = list(map(int, v.split(",")))
    for _ in range(100):
        p[0] += v[0]
        p[1] += v[1]
        p[0], p[1] = check_boundary(p)

    matrix[p[1]][p[0]] += 1


s = (int(wide/2), int(tall/2))

count = 0
mul = 1
for row in matrix[:s[1]]:
    count += sum(row[:s[0]])
mul *= count

count = 0
for row in matrix[:s[1]]:
    count += sum(row[s[0]+1:])
mul *= count

count = 0
for row in matrix[s[1]+1:]:
    count += sum(row[:s[0]])
mul *= count

count = 0
for row in matrix[s[1]+1:]:
    count += sum(row[s[0]+1:])
mul *= count

print(mul)