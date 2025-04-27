import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        if current_dist > distances[current]:
            continue
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

# Example usage
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 4)],
    'D': [('A', 5), ('B', 1), ('C', 4)]
}
print(dijkstra(graph, 'A'))