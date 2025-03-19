class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))
        if not self.directed:
            if v not in self.adjacency_list:
                self.adjacency_list[v] = []
            self.adjacency_list[v].append((u, weight))

    def is_directed(self):
        return self.directed

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for u in self.adjacency_list:
            for v, weight in self.adjacency_list[u]:
                edges.append((u, v, weight))
        return edges

    def get_neighbors(self, node):
        return [v for v, weight in self.adjacency_list.get(node, [])]

    def __str__(self):
        return str(self.adjacency_list)