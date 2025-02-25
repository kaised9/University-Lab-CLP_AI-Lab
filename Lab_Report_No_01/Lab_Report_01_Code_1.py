import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

    def __repr__(self):
        return f"({self.x}, {self.y})"

class DFS:
    def __init__(self, N):
        self.N = N
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        self.found = False
        self.goal_depth = 0
        self.grid = self.generate_grid()
        self.source, self.goal = self.generate_source_and_goal()
        self.visited = [[False for _ in range(N)] for _ in range(N)]
        self.path = []
        self.topological_order = []

    def generate_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]

    def generate_source_and_goal(self):
        while True:
            source = (random.randint(0, self.N-1), random.randint(0, self.N-1))  
            goal = (random.randint(0, self.N-1), random.randint(0, self.N-1) )  
            if self.grid[source[0]][source[1]] == 1 and self.grid[goal[0]][goal[1]] == 1 and source != goal:
                return Node(source[0], source[1], 0), Node(goal[0], goal[1], 0)

    def print_grid(self):
        print("Grid Are :")
        for row in self.grid:
            print(row)
        print(f"Source : {self.source}")
        print(f"Goal : {self.goal}")

    def is_valid(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.grid[x][y] == 1 and not self.visited[x][y]

    def dfs(self, node):
        self.visited[node.x][node.y] = True
        self.topological_order.append(node)
        self.path.append(node)

        if node.x == self.goal.x and node.y == self.goal.y:
            self.found = True
            self.goal_depth = node.depth
            return

        for dx, dy in self.directions:
            new_x = node.x + dx
            new_y = node.y + dy
            if self.is_valid(new_x, new_y):
                self.dfs(Node(new_x, new_y, node.depth + 1))
                if self.found:
                    return

        self.path.pop()

    def run(self):
        self.print_grid()
        self.dfs(self.source)
        if self.found:
            print("\nGoal Found !!!")
            print(f"Path: {self.path}")
            print(f"Number Of Moves : {self.goal_depth}")
        else:
            print("\nGoal Cannot  Reached !!!")
        print(f"Topological Order Of Node Traversal: {self.topological_order}")

if __name__ == "__main__":
    N = random.randint(4, 7)
    dfs_solver = DFS(N)
    dfs_solver.run()
