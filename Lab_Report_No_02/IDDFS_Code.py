class IDDFS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target
        self.n = len(grid)  
        self.m = len(grid[0])
        self.traversal_order = []
    
    def is_valid(self, x, y, visited):
        return 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] == 0 and not visited[x][y]

    def dls(self, x, y, depth, max_depth, visited):
        if depth > max_depth:
            return False
        if (x, y) == self.target:
            return True
        
        visited[x][y] = True
        self.traversal_order.append((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, visited):
                if self.dls(nx, ny, depth + 1, max_depth, visited):
                    return True

        return False

    def iddfs(self):
        max_depth_limit = 6 
        for depth in range(max_depth_limit + 1):  
            visited = [[False] * self.m for _ in range(self.n)]
            self.traversal_order.clear()
            if self.dls(self.start[0], self.start[1], 0, depth, visited):
                print(f"Path Found At Depth {depth} Using IDDFS")
                print(f"Traversal Order: {self.traversal_order}")
                return
        print(f"Path Not Found At Max Depth {max_depth_limit} Using IDDFS") 


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

sx, sy = map(int, input("Start : ").split())
tx, ty = map(int, input("Target : ").split())

iddfs_solver = IDDFS(grid, (sx, sy), (tx, ty))
iddfs_solver.iddfs()
