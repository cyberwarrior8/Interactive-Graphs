def bfs(graph, start):
    visited = set()
    queue = [start]
    traversal_order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            queue.extend(neighbor for neighbor in graph.get_neighbors(vertex) if neighbor not in visited)

    return traversal_order