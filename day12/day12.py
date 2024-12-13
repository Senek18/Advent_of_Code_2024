from collections import defaultdict

with open("day12/input.txt", "r") as f:
    matrix = [list(row) for row in f.read().splitlines()]

plants = set(cell for row in matrix for cell in row)
plot_sides = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

class Graph:
    def __init__(self, connections=None):
        self._graph = defaultdict(set)
        if connections:
            self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def dfs(self, start, visited):
        stack = [start]
        size = 0
        perimeter_size = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                perimeter_size += self.perimeter(node)
                visited.add(node)
                size += 1 
                stack.extend(self._graph[node] - visited) 
        return size, perimeter_size

    def connected_components(self):
        visited = set()
        components = []
        perimeter_list = []
        for node in self._graph:
            if node not in visited:
                size, perimeter_size = self.dfs(node, visited)
                components.append(size)
                perimeter_list.append(perimeter_size)
        return components, perimeter_list

    def is_node(self, node):
        return node in self._graph

    def area(self):
        return len(self._graph)

    def perimeter(self, node):
        return 4 - len(self._graph[node])

    def __str__(self):
        return f"{self.__class__.__name__}({dict(self._graph)})"

count = 0
for plant in plants:
    graphs_lib = []
    indices = [(i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row) if cell == plant]
    new_indices = indices.copy()
    connections = []
    for coord in indices:
        for move in plot_sides.values():
            neighbor = (coord[0] + move[0], coord[1] + move[1])
            if neighbor in indices:
                connections.append((coord, neighbor))
                try:
                    new_indices.remove(coord)
                except ValueError:
                    pass

    graph = Graph(connections)
    graph_count = graph.connected_components()
    component_sizes, perimeter_size = graph.connected_components()
    # print(f"Number of separate graphs for {plant}: {len(component_sizes)}")
    # print(f"Area of each graph: {component_sizes}")
    # print(f"Permieters of each graph: {perimeter_size}")
    for area, perimeter in zip(component_sizes, perimeter_size):
        count += area * perimeter
    if new_indices:
        count += len(new_indices) * 4

print(count)