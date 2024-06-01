def extract_min(visited, dist, n):
    min_dist = float('inf')
    min_index = -1
    for v in range(n):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[src] = 0
    visited = [False] * n
    prev = [-1] * n

    for _ in range(n):
        min_index = extract_min(visited, dist, n)
        u = min_index
        visited[u] = True
        if(u == end): break

        for v in range(n):
            new_dist = dist[u] + graph[u][v]
            if graph[u][v] > 0 and not visited[v] and dist[v] > new_dist:
                dist[v] = new_dist 
                prev[v] = u

    return prev

def traverse(prev,end,path = []):
    curr = end
    while(prev[curr] != -1):
        path.append(prev[curr])
        curr = prev[curr]
    else:
        path.reverse()
        path.append(end)
        print(path)


graph = [
    [0, 10, 20, 0, 0],
    [10, 0, 5, 15, 0],
    [20, 5, 0, 25, 30],
    [0, 15, 25, 0, 10],
    [0, 0, 30, 10, 0]
]
src = 0
end = 4
prev = dijkstra(graph, src, end)
traverse(prev, end)
