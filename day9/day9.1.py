with open("day9/input.txt", "r") as f:
    data = f.read()

filesystem = []
files = []
free_spaces = []

current_position = 0
for idx, i in enumerate(range(0, len(data), 2)):
    file_size = int(data[i])
    free_space_size = int(data[i+1]) if i+1 < len(data) else 0

    if file_size > 0:
        files.append((idx, file_size, current_position))
        filesystem.extend([idx] * file_size)
        current_position += file_size
    
    if free_space_size > 0:
        free_spaces.append((current_position, free_space_size))
        filesystem.extend(["."] * free_space_size)
        current_position += free_space_size

files = sorted(files, key=lambda x: x[0], reverse=True)

for file_id, file_size, file_position in files:
    for i, (space_start, space_size) in enumerate(free_spaces):
        if space_size >= file_size and space_start < file_position:
            filesystem[space_start:space_start + file_size] = [file_id] * file_size
            filesystem[file_position:file_position + file_size] = ["."] * file_size
            free_spaces[i] = (space_start + file_size, space_size - file_size)
            free_spaces.append((file_position, file_size))
            break


count = 0
for idx, i in enumerate(filesystem):
    if i != ".":
        count += idx * i

print(count)


    