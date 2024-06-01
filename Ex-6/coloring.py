class Vertex:
    def __init__(self, val, color = None):
        self.val = val
        self.color = color

class Graph:
    
        
    def __init__(self, adj_matrix):
        self.mat = adj_matrix
        self.n = len(adj_matrix)
        self.vertices = [Vertex(i) for i in range(self.n)]

    
    def adj(self, vertex: Vertex):
        return [self.vertices[i] for i in range(self.n) if self.mat[vertex.val][i] > 0]
    
    def color_adj(self, vertex: Vertex):
        adj_verts = self.adj(vertex)
        adj_colors = [vertex.color for vertex in adj_verts if vertex.color != None]
        return adj_colors
    
        

def coloring(graph: Graph, k: int, i:int = 0):
    if(i >= graph.n): return True
    curr_ver = graph.vertices[i]
    adj_colors = graph.color_adj(curr_ver)
    for color in range(k):
        if color in adj_colors: continue
        curr_ver.color = color
        possible = coloring(graph, k, i + 1)
        if(possible): return True
        curr_ver.color = None
    return False
        
if __name__ == "__main__":
    adj_matrix = [
    [0, 1, -1, -1, 2],
    [1, 0, 3, -1, -1],
    [-1, 3, 0, 4, -1],
    [-1, -1, 4, 0, 5],
    [2, -1, -1, 5, 0]
]
    graph = Graph(adj_matrix)
    print(coloring(graph, 2))
    
        
