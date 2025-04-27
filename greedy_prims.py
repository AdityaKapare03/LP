import heapq
# Graph with edges and weights
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('A', 5), ('B', 2), ('D', 1)],
    'D': [('B', 4), ('C', 1)]
}

def prim_optimized(start):
    visited = set()
    edges = []
    # Priority queue: (weight, from, to)
    heap = []
    visited.add(start)
    
    # Initialize heap with edges from the start node
    for to, weight in graph[start]:
        heapq.heappush(heap, (weight, start, to))
    
    while heap and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(heap)
        if to not in visited:
            print(f"{frm} - {to}: {weight}")
            visited.add(to)
            # Add edges from the newly visited node
            for neighbor, neighbor_weight in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_weight, to, neighbor))

prim_optimized('A')