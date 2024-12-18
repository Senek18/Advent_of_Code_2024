from collections import defaultdict
import heapq
from tqdm import tqdm

with open("day18/input.txt", "r") as f:
    data = f.read().splitlines()
size = 70
matrix = [["." for _ in range(size+1)] for _ in range(size+1)]


# for row in matrix:
#     print("".join(row))

class Graph:
    def __init__(self, connections=None):
        self._graph = defaultdict(dict)
        if connections:
            self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, node1, node2, weight):
        self._graph[node1][node2] = weight
        self._graph[node2][node1] = weight
    
    def find_shortest_path(self, start, end):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            cost, node, path = heapq.heappop(queue)

            if node in visited:
                continue

            visited.add(node)
            path = path + [node]

            if node == end:
                return cost

            for neighbor, weight in self._graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return float('inf') 

    
    def __str__(self):
        return f"{self.__class__.__name__}({dict(self._graph)})"

def check_boundry(x,y):
    if x < 0 or x > size:
        return False
    if y < 0 or y > size:
        return False
    return True

moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def check_bit(stop):
    for i, row in enumerate(data):
        if i==stop:
            break

        x,y = map(int, row.split(","))
        matrix[y][x] = "#"

    graph = Graph()
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == "#":
                continue

            for dx,dy in moves:
                if check_boundry(x+dx, y+dy) and matrix[y+dy][x+dx] == "." :
                    graph.add((x,y), (x+dx,y+dy), 1)
    
    if graph.find_shortest_path((0,0),(size,size)) == float('inf'):
        return (True, i)
    
    return False, i

for i in tqdm(range(len(data))):
    check, idx = check_bit(i)
    if check:
        print("IDX: ",i)
        print("CORD: ",data[idx-1])
        break




        
