with open("day4/input.txt", "r") as f:
    matrix = [list(line) for line in f.read().splitlines()]


index_list = [(idx, jdx) for idx, row in enumerate(matrix) for jdx, letter in enumerate(row) if letter == "X"]

moves = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),
    "upright": (-1, 1), "upleft": (-1, -1), "downright": (1, 1), "downleft": (1, -1)
}

count = 0

for x in index_list:
    for move in moves.values():
        try:
            row, cell = x[0], x[1]
            for i in range(1, 4):
                row += move[0]
                cell += move[1]
                if row < 0 or cell < 0 or matrix[row][cell] != "MAS"[i-1]:
                    break
            else:
                count += 1
        except IndexError:
            pass

print(count)
