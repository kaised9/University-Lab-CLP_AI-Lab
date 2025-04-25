import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

# Manhattan Distance.
def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# KMeans Clustering with Manhattan Distance.
class KMeans:
    def __init__(self, points, clusters, size=11):
        self.points = points
        self.clusters = clusters
        self.grid_size = size

        all_coords = [(x, y) for x in range(size) for y in range(size)]
        random.shuffle(all_coords)
        if points > len(all_coords):
            raise ValueError("Grid Too Small For Unique Points")
        self.p = [Point(x, y) for x, y in all_coords[:points]]
        self.k = [Point(random.randint(0, size-1), random.randint(0, size-1)) for _ in range(clusters)]

        self.start()

    def start(self):
        while True:
            for point in self.p:
                distances = [manhattan_distance(point, center) for center in self.k]
                point.cluster = distances.index(min(distances))

            old_k = [Point(center.x, center.y) for center in self.k]

            for i in range(self.clusters):
                cluster_points = [p for p in self.p if p.cluster == i]
                if cluster_points:
                    avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                    avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                    self.k[i].x = avg_x
                    self.k[i].y = avg_y

            if all(k.x == old_k[i].x and k.y == old_k[i].y for i, k in enumerate(self.k)):
                break

        self.visualize()

    def visualize(self):
        grid = [[" " for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for p in self.p:
            grid[p.y][p.x] = str(p.cluster)

        for i, c in enumerate(self.k):
            grid[c.y][c.x] = chr(65 + i)

        print("\nCluster Visualization Are Given Below:\n")
        x_labels = [f"{i:02}" for i in range(self.grid_size)]
        print("     " + "    ".join(x_labels))
        for idx, row in enumerate(grid):
            line = "    ".join(cell if cell != " " else "." for cell in row)
            print(f"{idx:02}   {line}")
            
def main():
    kmeans = KMeans(points=100, clusters=10, size=11)

if __name__ == "__main__":
    main()
