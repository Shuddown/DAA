import numpy as np

def nearest_neighbour_tsp(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    path = [start_vertex]
    current_vertex = start_vertex
    visited[current_vertex] = True
    total_cost = 0

    for _ in range(n - 1):
        nearest_neighbour = None
        min_distance = float('inf')
        for next_vertex in range(n):
            if not visited[next_vertex] and graph[current_vertex][next_vertex] < min_distance:
                nearest_neighbour = next_vertex
                min_distance = graph[current_vertex][next_vertex]
        
        path.append(nearest_neighbour)
        visited[nearest_neighbour] = True
        total_cost += min_distance
        current_vertex = nearest_neighbour

    total_cost += graph[current_vertex][start_vertex]
    path.append(start_vertex)

    return total_cost, path

graph = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

start_vertex = 0
best_cost, best_path = nearest_neighbour_tsp(graph, start_vertex)

print(f"Total cost: {best_cost}")
print(f"Path: {best_path}")
