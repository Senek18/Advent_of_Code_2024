from tqdm import tqdm

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
potential_obstacles = {}

while True:
    guard_matrix[point[0]][point[1]] = 1
    potential_obstacles[point] = potential_obstacles.get(point, []) + [move]
    point = (point[0] + moves[move][0], point[1] + moves[move][1])

    if not check_boundary(point[0], point[1]):
        break

    if point in obstacles_cords:
        point = (point[0] - moves[move][0], point[1] - moves[move][1])
        move = rotation[move]
        continue

cords = []
for key, values in tqdm(potential_obstacles.items()):
    for spot in values:
        point = start_point
        move = "up"
        obstacle = (key[0] + moves[spot][0], key[1] + moves[spot][1])

        if not check_boundary(obstacle[0], obstacle[1]) or (obstacle in obstacles_cords) or obstacle == start_point:
            continue

        new_obstacles_cords = obstacles_cords + [obstacle]
        new_guard_matrix = [[0 for _ in range(col_dim)] for _ in range(row_dim)]

        while True:
            new_guard_matrix[point[0]][point[1]] += 1

            if new_guard_matrix[point[0]][point[1]] > 10:
                cords.append(obstacle)
                break

            point = (point[0] + moves[move][0], point[1] + moves[move][1])

            if not check_boundary(point[0], point[1]):
                break

            if point in new_obstacles_cords:
                point = (point[0] - moves[move][0], point[1] - moves[move][1])
                move = rotation[move]
                continue

print(len(list(set(cords))))