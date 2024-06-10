import numpy as np

class TSPMSTSolver:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def find_mst(self):
        mst = np.zeros_like(self.graph)  # Initialize MST with zeros
        visited = [False] * self.n
        key = [float('inf')] * self.n
        parent = [-1] * self.n

        key[0] = 0

        for _ in range(self.n):
            u = self.min_key(key, visited)
            visited[u] = True

            for v in range(self.n):
                if self.graph[u][v] > 0 and not visited[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        for i in range(1, self.n):
            mst[i][parent[i]] = self.graph[i][parent[i]]
            mst[parent[i]][i] = self.graph[i][parent[i]]

        return mst

    def min_key(self, key, visited):
        min_val = float('inf')
        min_index = -1

        for i in range(len(key)):
            if not visited[i] and key[i] < min_val:
                min_val = key[i]
                min_index = i

        return min_index

    def preorder_traversal(self, u, visited, tour):
        visited[u] = True
        tour.append(u)

        for v in range(self.n):
            if self.graph[u][v] > 0 and not visited[v]:
                self.preorder_traversal(v, visited, tour)

    def tsp_mst(self):
        mst = self.find_mst()

        tour = []
        visited = [False] * self.n
        self.preorder_traversal(0, visited, tour)

        tour.append(tour[0])

        total_cost = sum(self.graph[tour[i]][tour[i+1]] for i in range(len(tour)-1))

        return total_cost, tour

graph = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

solver = TSPMSTSolver(graph)
total_cost, tsp_tour = solver.tsp_mst()
print("Total Cost:", total_cost)
print("TSP Tour:", tsp_tour)
