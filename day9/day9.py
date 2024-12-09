with open("day9/input.txt", "r") as f:
    data = f.read()

filesystem = []
for idx, i in enumerate(range(0, len(data), 2)):
    file_size = int(data[i])
    free_space_size = int(data[i+1]) if i+1 < len(data) else 0

    if file_size > 0:
        filesystem.extend([idx] * file_size)
    
    if free_space_size > 0:
        filesystem.extend(["."] * free_space_size)

point = len(filesystem)

while True:
    point -= 1
    jdx = filesystem.index(".")
    filesystem[point], filesystem[jdx] = filesystem[jdx], filesystem[point]

    if point < jdx:
        break


filesystem.remove(".")

count = 0

for idx, i in enumerate(filesystem):
    if i == ".":
        break
    count += idx * i

print(count)


    