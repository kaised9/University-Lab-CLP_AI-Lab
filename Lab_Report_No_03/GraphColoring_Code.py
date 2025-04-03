class GraphColoring:
    def __init__(self, V, graph, num_colors):
        self.V = V 
        self.num_colors = num_colors  
        self.graph = graph  
        self.color = [-1] * self.V  

    def is_possible(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.color[i] == c:
                return False
        return True

    def solve(self, v):
       
        if v == self.V:
            return True

        for c in range(1, self.num_colors + 1):
            if self.is_possible(v, c):
                
                self.color[v] = c

                if self.solve(v + 1):
                    return True

                self.color[v] = -1

        return False
    
    def graph_color(self):
        if self.solve(0):
            print("Coloring Possible with", self.num_colors, "Colors")
            print("Color Assignment:", self.color)
        else:
            print("Coloring Not Possible with", self.num_colors, "Colors")

if __name__ == "__main__":
    
    N, M, K = map(int, input().split())
    graph = [[0] * N for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1 
        
    graph_coloring = GraphColoring(N, graph, K)
    graph_coloring.graph_color()
