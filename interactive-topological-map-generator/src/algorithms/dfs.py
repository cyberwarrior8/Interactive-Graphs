def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            stack.extend(neighbor for neighbor in graph.get_neighbors(vertex) if neighbor not in visited)

    return traversal_order