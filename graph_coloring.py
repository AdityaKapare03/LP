def graph_coloring(graph, colors):
    color_map = {}
    def can_color(node, color):
        return all(color_map.get(neigh) != color for neigh in graph[node])
    
    def backtrack(node):
        if node not in color_map:
            for color in colors:
                if can_color(node, color):
                    color_map[node] = color
                    if all(backtrack(neigh) for neigh in graph[node]):
                        return True
                    del color_map[node]
            return False
        return True
    
    for node in graph:
        if not backtrack(node):
            return None
    return color_map

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
print(graph_coloring(graph, ['Red', 'Green', 'Blue']))