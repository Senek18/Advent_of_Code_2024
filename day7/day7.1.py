from itertools import product
from tqdm import tqdm

with open("day6/input.txt", "r") as f:
    data = f.read().splitlines()
    final = {}
    for row in data:
        splits = row.split(": ")
        final[int(splits[0])]= list(map(int, splits[1].split(" ")))

count = 0
operaators = ["+", "*", "||"]

for key, values in tqdm(final.items()):
    lenght = len(values)-1
    possible_combination = list(product(operaators, repeat=lenght))
    
    for combination in possible_combination:
        if combination[0] == "+":
            target = values[0] + values[1]
        elif combination[0] == "*":
            target = values[0] * values[1]
        elif combination[0] == "||":
            target = int(f"{values[0]}{values[1]}")

        for i in range(2,lenght+1):
            if combination[i-1] == "+":
                target += values[i]
            elif combination[i-1] == "*":
                target *= values[i]
            elif combination[i-1] == "||":
                target = int(f"{target}{values[i]}")
            
            if target > key:
                break
        
        if target == key:
            count += key
            break

print(count)
                    

            

