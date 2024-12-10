with open("day10/input.txt", "r") as f:
    data = f.read().splitlines()
    matrix = [[int(cell) for cell in row] for row in data]

zero_index = [(idx, jdx) for idx, row in enumerate(matrix) for jdx, cell in enumerate(row) if cell == 0]
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

def make_move_and_check_value(point, move, val):
    row, col = point
    row += moves[move][0]
    col += moves[move][1]
    if row < 0 or row >= len(matrix):
        return None
    if col < 0 or col >= len(matrix[0]):
        return None

    try:
        if matrix[row][col] == val:
            return (row, col)
    except IndexError:
        return None

    return None

def find_all_points(point_list, val):
    new_list = []
    for point in point_list:
        for key, move in moves.items():
            if new_point:=make_move_and_check_value(point, key, val):
                new_list.append(new_point)
    return new_list

point_dict = {0: zero_index}
for i in range(1, 10):
    point_dict[i] = find_all_points(point_dict[i-1], i)

print(len(point_dict[9]))
