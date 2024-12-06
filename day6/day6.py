with open("day6/input.txt", "r") as f:
    data = f.read().splitlines()

obstacles_cords = [ (rix, cix) for rix, row in enumerate(data) for cix, cell in enumerate(row) if cell == "#"]
start_point = [ (rix, cix) for rix, row in enumerate(data) for cix, cell in enumerate(row) if cell == "^"][0]

row_dim = len(data)
col_dim = len(data[0])

guard_matrix = [[0 for _ in range(col_dim)] for _ in range(row_dim)]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
rotation = {"up": "right", "right": "down", "down": "left", "left": "up"}

def check_boundary(row, col):
    if row < 0 or row >= row_dim:
        return False
    if col < 0 or col >= col_dim:
        return False
    return True

point = start_point
move = "up"
while True:
    guard_matrix[point[0]][point[1]] = 1
    point = (point[0] + moves[move][0], point[1] + moves[move][1])

    if not check_boundary(point[0], point[1]):
        break

    if point in obstacles_cords:
        point = (point[0] - moves[move][0], point[1] - moves[move][1])
        move = rotation[move]
        continue

print(sum([sum(row) for row in guard_matrix]))