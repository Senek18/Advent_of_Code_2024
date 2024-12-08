from itertools import combinations

with open("day8/input.txt", "r") as f:
    data = f.read().splitlines()
    antennas = {char for row in data for char in row if char != '.'}

nodes_matrix = [[0 for _ in row] for row in data]

row_dim = len(data)
col_dim = len(data[0])

def check_boundary(row, col):
    if row < 0 or row >= row_dim:
        return False
    if col < 0 or col >= col_dim:
        return False
    return True

antennas_cord = {}
for antenna in antennas:
    antennas_cord[antenna] = [(rix, cix) for rix, row in enumerate(data) for cix, cell in enumerate(row) if cell == antenna]


def distance_vector(point1, point2):
    return point1[0] - point2[0], point1[1] - point2[1]

for key, value in antennas_cord.items():
    all_combinations = combinations(value, 2)
    for point1, point2 in all_combinations:
        nodes_matrix[point1[0]][point1[1]] = 1
        nodes_matrix[point2[0]][point2[1]] = 1
        vectore = distance_vector(point1, point2)
        nodes_p1 = point1[0]+vectore[0], point1[1]+vectore[1]
        nodes_p2 = point2[0]-vectore[0], point2[1]-vectore[1]

        while True:
            if check_boundary(nodes_p1[0], nodes_p1[1]):
                nodes_matrix[nodes_p1[0]][nodes_p1[1]] = 1
            else:
                break
            nodes_p1 = nodes_p1[0]+vectore[0], nodes_p1[1]+vectore[1]
        
        while True:
            if check_boundary(nodes_p2[0], nodes_p2[1]):
                nodes_matrix[nodes_p2[0]][nodes_p2[1]] = 1
            else:
                break
            nodes_p2 = nodes_p2[0]-vectore[0], nodes_p2[1]-vectore[1]
        
        

print(sum([sum(row) for row in nodes_matrix]))