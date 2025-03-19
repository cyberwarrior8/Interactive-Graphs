import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    min_dist = {start: 0}

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue

        path = path + [node]
        seen.add(node)

        if node == end:
            return (cost, path)

        for neighbor, weight in graph.adjacency_list.get(node, []):
            if neighbor in seen:
                continue
            prev = min_dist.get(neighbor, None)
            next = cost + weight
            if prev is None or next < prev:
                min_dist[neighbor] = next
                heapq.heappush(queue, (next, neighbor, path))

    return float("inf"), []