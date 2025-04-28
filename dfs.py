def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

def input_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    for _ in range(nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by spaces: ").split()
        graph[node] = neighbors
    return graph

graph = input_graph()

initial = input("Enter the starting nod: ")
print(f"DFS starting from '{initial}':")
dfs(graph, initial)