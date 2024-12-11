from functools import cache
from tqdm import tqdm
with open("day11/input.txt", "r") as f:
    data = f.read().split(" ")
print(data)


@cache
def score(stone, blinks, limit):
    if blinks == limit:
        return 1
    if stone == "0":
        return score("1", blinks+1, limit)
    elif (stone_len:=len(stone)) % 2 == 0:
        stone_l = stone[:int(stone_len/2)]
        stone_r= str(int(stone[int(stone_len / 2):]))
        return score(stone_l, blinks+1, limit) + score(stone_r, blinks+1, limit)
    return score(str(int(stone)*2024), blinks+1, limit)

for idx, limit in enumerate([25, 75]):
    count = 0
    for i in tqdm(data):
        count += score(i, 0, limit)

    print(f"Part {idx+1}:", count)