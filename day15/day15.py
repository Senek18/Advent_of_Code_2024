with open("day15/input.txt", "r") as f:
    data = f.read().split("\n\n")

warehouse = [[cell for cell in row] for row in data[0].split("\n")]
moves_list = ""
for row in data[1].split("\n"):
    moves_list += row

moves = {"^":(-1, 0), "v":(1,0), "<":(0,-1), ">":(0,1)}
robot_position = [[i, j] for i, row in enumerate(warehouse) for j, cell in enumerate(row) if cell == "@"][0]

def matrxi_print(matrix):
    for row in matrix:
        print(" ".join([str(x) for x in row]))

for move in moves_list:
    boxs_cord = []
    space_check = robot_position
    while True:
        space_check = [space_check[0] + moves[move][0], space_check[1] + moves[move][1]]
        if warehouse[space_check[0]][space_check[1]] == ".":
            if boxs_cord:
                for box in boxs_cord:
                    warehouse[box[0] + moves[move][0]][box[1] + moves[move][1]] = "O"
            warehouse[robot_position[0] + moves[move][0]][robot_position[1] + moves[move][1]] = "@"
            warehouse[robot_position[0]][robot_position[1]] = "."
            robot_position = [robot_position[0] + moves[move][0], robot_position[1] + moves[move][1]]
            break
        elif warehouse[space_check[0]][space_check[1]] == "O":
            boxs_cord.append(space_check)
        elif warehouse[space_check[0]][space_check[1]] == "#":
            break

boxes = [[i, j] for i, row in enumerate(warehouse) for j, cell in enumerate(row) if cell == "O"]
count = 0
for y, x in boxes:
    count += (y * 100 + x)


matrxi_print(warehouse)
print(count)