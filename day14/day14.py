import re

with open("day14/input.txt", "r") as f:
    data = f.read().splitlines()

wide, tall = 101, 103
matrix = [[0] * wide for _ in range(tall)]

def check_boundary(p):
    return p[0] % wide, p[1] % tall

for line in data:
    p, v = re.findall(r"-?\d+,-?\d+", line)
    p = list(map(int, p.split(",")))
    v = list(map(int, v.split(",")))
    
    for _ in range(100):
        p[0] += v[0]
        p[1] += v[1]
        p[0], p[1] = check_boundary(p)
    
    matrix[p[1]][p[0]] += 1

s = (wide // 2, tall // 2)

quadrants = [
    sum(sum(row[:s[0]]) for row in matrix[:s[1]]),          
    sum(sum(row[s[0]+1:]) for row in matrix[:s[1]]),        
    sum(sum(row[:s[0]]) for row in matrix[s[1]+1:]),       
    sum(sum(row[s[0]+1:]) for row in matrix[s[1]+1:]),       
]

mul = 1
for q in quadrants:
    mul *= q

print(mul)