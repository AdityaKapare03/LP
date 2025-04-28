import heapq

def astar(graph, start, goal, heuristic):
    closed_set = set()
    open_list = [(0 + heuristic[start], 0, start)]
    parents={start:None}
    g_values={start:0}

    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        
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
    'B': {'A': 1, 'D': 2, 'E': 3},
    'C': {'A': 3, 'F': 3},
    'D': {'B':2, 'G':4},
    'E': {'B':3, 'H':2},
    'F':{'C':3, 'H':3},
    'G':{'D':4, 'H':1}, 
    'H':{'F':3, 'G':1, 'E':2}
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 4, 'E': 3, 'F': 2,
    'G': 1, 'H': 0  
}

print("A* path from A to H:")
print(astar(graph, 'A', 'H', heuristic))