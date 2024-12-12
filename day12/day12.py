from collections import defaultdict

with open("day12/input.txt", "r") as f:
    data = f.read().splitlines()
    matrix = [[cell for cell in row] for row in data]
plants = tuple({cell for row in data for cell in row})
plot_sides = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def is_node(self, node):
        return node in self._graph

    def return_area(self):
        if self._graph:
            return len(self._graph)
        return 1

    def return_perimeter(self):
        if self._graph:
            count = 0
            for key, value in self._graph.items():
                count += (4 - len(value))
            return count
        return 4

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


count = 0
for plant in ["C"]:
    graphs_lib = []
    index = [(idx, jdx) for idx, row in enumerate(matrix) for jdx, cell in enumerate(row) if cell == plant]
    for cord in index:
        connections = []
        for key, move in plot_sides.items():
            new_cord = (cord[0] + move[0], cord[1] + move[1])
            if new_cord in index and (new_cord, cord) not in connections:
                connections.append((cord, new_cord))
        if not graphs_lib:
            graphs_lib.append(Graph(connections))
        else:
            stop = False
            for graph in graphs_lib:
                for temp in connections:
                    if graph.is_node(temp[0]) or graph.is_node(temp[1]):
                        graph.add_connections(connections)
                        stop = True
                        break
                if stop:
                    break
            else:
                graphs_lib.append(Graph(connections))

    for graph in graphs_lib:
        print(plant, graph.return_area(), graph.return_perimeter())
        count += (graph.return_perimeter() * graph.return_area())

print(count)