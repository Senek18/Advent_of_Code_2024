with open("input.txt", "r") as f:
    data = f.read().split(" ")
print(data)

def rules_book(stone):
    if stone == "0":
        return ["1"]
    elif (stone_len:=len(stone)) % 2 == 0:
        stone_l = stone[:int(stone_len/2)]
        stone_r= str(int(stone[int(stone_len / 2):]))

        return [stone_l, stone_r ]
    else:
        return [str(int(stone)*2024)]

old_arrangement = data
new_arrangement=[]
for i in range(25):
    for stone in old_arrangement:
        new_arrangement += rules_book(stone)
    old_arrangement = new_arrangement
    new_arrangement = []

print(len(old_arrangement))