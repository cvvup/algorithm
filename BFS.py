from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set() 
    queue = deque([(start, [start])])  

    while queue:
        vertex, path = queue.popleft()  
        if vertex not in visited:
            visited.add(vertex) 
            for neighbor in graph[vertex]:
                if neighbor == goal: 
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor])) 

    return None  

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

path_A_to_F = bfs_shortest_path(graph, 'A', 'F')
path_F_to_B = bfs_shortest_path(graph, 'F', 'B')

print("Кратчайший путь от A до F:", path_A_to_F)
print("Кратчайший путь от F до B:", path_F_to_B)
