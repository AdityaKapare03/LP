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
print("\nThis is recursive BFS... \nBFS starting from 'a':")
call_bfs(graph, 'a')