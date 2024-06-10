import numpy as np
from collections import deque

def solve_TSP(graph, start_vertex):
    n = len(graph)
    best_cost = float('inf')
    best_path = []

    def calculate_initial_bound():
        bound = 0
        for i in range(n):
            min1, min2 = float('inf'), float('inf')
            for j in range(n):
                if i != j:
                    if graph[i][j] < min1:
                        min2 = min1
                        min1 = graph[i][j]
                    elif graph[i][j] < min2:
                        min2 = graph[i][j]
            bound += (min1 + min2) / 2
        return bound

    def calculate_bound(path, current_cost, new_cost, next_vertex):
        bound = new_cost
        remaining_vertices = set(range(n)) - set(path)
        for vertex in remaining_vertices:
            min_edge = min([graph[vertex][i] for i in remaining_vertices if i != vertex], default=0)
            bound += min_edge
        return bound

    initial_bound = calculate_initial_bound()
    initial_path = [start_vertex]
    initial_state = (initial_bound, 0, start_vertex, initial_path, set([start_vertex]))
    
    queue = deque([initial_state])

    while queue:
        current_bound, current_cost, current_vertex, current_path, visited = queue.popleft()
        
        if current_cost >= best_cost:
            continue

        if len(current_path) == n:
            final_cost = current_cost + graph[current_vertex][start_vertex]
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = current_path + [start_vertex]
            continue

        for next_vertex in range(n):
            if next_vertex not in visited:
                new_visited = visited | {next_vertex}
                new_path = current_path + [next_vertex]
                new_cost = current_cost + graph[current_vertex][next_vertex]
                new_bound = calculate_bound(current_path, current_cost, new_cost, next_vertex)
                if new_bound < best_cost:
                    new_state = (new_bound, new_cost, next_vertex, new_path, new_visited)
                    queue.append(new_state)

    return best_cost, best_path
