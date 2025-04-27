import heapq

def astar(graph, start, goal, heuristic):
    open_list = [(0 + heuristic[start], 0, start)]  # (f, g, node)
    closed_set = set()
    g_values = {start: 0}
    parents = {start: None}
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Reverse path
            
        if current in closed_set:
            continue
            
        closed_set.add(current)
        
        for neighbor, cost in graph[current].items():
            if neighbor in closed_set:
                continue
                
            tentative_g = g + cost
            
            if neighbor not in g_values or tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, tentative_g, neighbor))
                parents[neighbor] = current
    
    return None  

# Example usage (finding path in a grid)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2, 'E': 4},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 2, 'G': 3},
    'E': {'B': 4, 'H': 1},
    'F': {'C': 2, 'H': 5},
    'G': {'D': 3, 'H': 2},
    'H': {'E': 1, 'F': 5, 'G': 2}
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 4, 'E': 3, 'F': 2,
    'G': 1, 'H': 0  
}

print("A* path from A to H:")
print(astar(graph, 'A', 'H', heuristic))