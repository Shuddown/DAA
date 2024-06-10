import numpy as np
import matplotlib.pyplot as plt
import time
import heapq
from collections import deque



def generate_random_graph(n):
    graph = np.random.randint(1, 100, size=(n, n))
    graph = np.tril(graph) + np.tril(graph, -1).T  
    np.fill_diagonal(graph, 0) 
    return graph

def analyze_tsp_solvers(solver_functions):
    graph_sizes = list(range(1, 111))

    times = [[] for _ in range(len(solver_functions))]

    for n in graph_sizes:
        graph = generate_random_graph(n)
        for i, solver_func in enumerate(solver_functions):
            start_time = time.perf_counter()
            solver_func(graph, 0)
            end_time = time.perf_counter()
            times[i].append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    for i, time_list in enumerate(times):
        plt.plot(graph_sizes, time_list, label=solver_functions[i].__name__)

    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Analysis of TSP Solvers')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')

    plt.savefig('tsp_solver_analysis.png')

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

def bb_best(graph, start_vertex):
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
    
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)

    while priority_queue:
        current_bound, current_cost, current_vertex, current_path, visited = heapq.heappop(priority_queue)
        
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
                    heapq.heappush(priority_queue, new_state)

    return best_cost, best_path

def bb_bfs(graph, start_vertex):
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

    

def solve_TSP_MST(graph, start_vertex):
    n = len(graph)

    def find_mst():
        mst = np.zeros_like(graph)  
        visited = [False] * n
        key = [float('inf')] * n
        parent = [-1] * n

        key[0] = 0

        for _ in range(n):
            u = min_key(key, visited)
            visited[u] = True

            for v in range(n):
                if graph[u][v] > 0 and not visited[v] and graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u

        for i in range(1, n):
            mst[i][parent[i]] = graph[i][parent[i]]
            mst[parent[i]][i] = graph[i][parent[i]]

        return mst

    def min_key(key, visited):
        min_val = float('inf')
        min_index = -1

        for i in range(len(key)):
            if not visited[i] and key[i] < min_val:
                min_val = key[i]
                min_index = i

        return min_index

    def preorder_traversal(u, visited, tour):
        visited[u] = True
        tour.append(u)

        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                preorder_traversal(v, visited, tour)

    mst = find_mst()

    tour = []
    visited = [False] * n
    preorder_traversal(0, visited, tour)

    tour.append(tour[0])

    total_cost = sum(graph[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return total_cost, tour
def analyze_tsp_accuracy(solver_functions):
    graph_sizes = list(range(1, 111))

    accuracy_ratios = [[] for _ in range(len(solver_functions))]

    for n in graph_sizes:
        graph = generate_random_graph(n)
        accurate_cost, _ = solver_functions[0](graph,0)  
        for i, solver_func in enumerate(solver_functions):
            if i == 0:
                accuracy_ratios[i].append(1)  
            else:
                cost, _ = solver_func(graph,0)
                accuracy_ratio = cost / accurate_cost
                accuracy_ratios[i].append(accuracy_ratio)

    plt.figure(figsize=(10, 6))
    for i, accuracy_list in enumerate(accuracy_ratios):
        plt.plot(graph_sizes, accuracy_list, label=solver_functions[i].__name__)

    plt.xlabel('Number of Vertices')
    plt.ylabel('Accuracy Ratio')
    plt.title('Accuracy Ratio Analysis of TSP Solvers')
    plt.legend()
    plt.xscale('log')

    plt.savefig('tsp_solver_accuracy_analysis.png')

 
analyze_tsp_solvers([bb_best, nearest_neighbour_tsp,solve_TSP_MST, bb_bfs])
analyze_tsp_accuracy([bb_best, nearest_neighbour_tsp,solve_TSP_MST, bb_bfs])
