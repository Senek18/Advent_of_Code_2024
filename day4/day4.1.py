with open("day4/input.txt", "r") as f:
    matrix = [list(line) for line in f.read().splitlines()]


index_list = [(idx, jdx) for idx, row in enumerate(matrix) for jdx, letter in enumerate(row) if letter == "A"]

moves = {"upright": (-1, 1), "upleft": (-1, -1), "downright": (1, 1), "downleft": (1, -1)}

possible_moves = {"d1": ["downleft", "upright"],
                  "d2": ["upleft", "downright"]}

count = 0

for x in index_list:
    d1, d2=False, False
    row, cell = x[0], x[1]

    a_row = row + moves["downleft"][0]
    b_row = row + moves["upright"][0]
    c_row = row + moves["upleft"][0]
    d_row = row + moves["downright"][0]

    a_cell = cell + moves["downleft"][1]
    b_cell = cell + moves["upright"][1]
    c_cell = cell + moves["upleft"][1]
    d_cell = cell + moves["downright"][1]

    if a_row < 0 or b_row < 0 or c_row < 0 or d_row < 0 or a_cell < 0 or b_cell < 0 or c_cell < 0 or d_cell < 0:
        continue

    try:
        if (matrix[a_row][a_cell] == "M" and matrix[b_row][b_cell] == "S") \
        or (matrix[a_row][a_cell] == "S" and matrix[b_row][b_cell] == "M"):
            d1 = True

        if (matrix[c_row][c_cell] == "M" and matrix[d_row][d_cell] == "S") \
        or (matrix[c_row][c_cell] == "S" and matrix[d_row][d_cell] == "M"):
            d2 = True
    
        if d1 and d2:
            count += 1
    except IndexError:
        pass

print(count)
