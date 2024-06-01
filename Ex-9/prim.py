
def prim(graph):
    
    n = len(graph)
    key = [float('inf')] * n
    parent = [-1] * n
    key[0] = 0
    mst_set = [False] * n

    for _ in range(n):
        min_key = float('inf')
        min_index = -1

        for v in range(n):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        u = min_index
        mst_set[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    mst = []
    for i in range(1, n):
        mst.append((parent[i], i, graph[i][parent[i]]))
    return mst

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
print("Prim's Algorithm: ", prim(graph))
