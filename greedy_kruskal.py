def kruskal(graph):
    parent = {}
    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u
    def union(u, v):
        parent[find(u)] = find(v)
    
    mst = []
    edges = sorted((w, u, v) for u in graph for v, w in graph[u])
    for node in graph:
        parent[node] = node
    
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
    return mst

# Example usage
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 4)],
    'D': [('A', 5), ('B', 1), ('C', 4)]
}
print(kruskal(graph))