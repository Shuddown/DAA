from copy import deepcopy

def floyd_warshall(graph):
    cpy = deepcopy(graph)
    for k in range(len(cpy)):
        for i in range(len(cpy)):
            for j in range(len(cpy)):
                    cpy[i][j] = min(cpy[i][k] + cpy[k][j], cpy[i][j])
    return cpy
    

graph = [
    [1,float('inf'),1,2],
    [4, 1, float('inf'), 3],
    [5,3,4,6],
    [3,9,2,float('inf')]
]
print(graph)
print(floyd_warshall(graph))