def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

def bfsr(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return visited
    
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
        
    bfsr(graph, queue, visited)

    return visited

def call_bfs(graph, start):
    visited = set([start])
    queue = [start]
    visited.add(start)
    return bfsr(graph, queue, visited)
    
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited


# Example usage
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

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
print("\nNormal BFS... ")
print(f"BFS starting from '{initial}':")
bfs(graph, initial)
print("\nThis is recursive BFS... \nBFS starting from 'a':")
call_bfs(graph, 'a')