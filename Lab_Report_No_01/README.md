# TITLE OF THE PROBLEM :
Write a program that generates a random N×N grid (N between 4 and 7) with non-obstacle source and goal states. It performs DFS to find a path from source to goal and prints the grid, source, goal, DFS path, and topological order of node traversal.



# PROCEDURE/ANALYSIS : 

1. Grid Generation:
   
i. A grid of size N×N is created with random values (0 or 1). Where '1' represents a free cell and '0' represents an obstacle.

ii. A start (source) and end (goal) point are randomly chosen. Both must be free cells and different from each other.


2. DFS Implementation:
   
i. DFS starts from the source and explores all possible paths recursively.

ii. It moves in four directions: up, down, left, and right.

iii. It checks if the next cell is valid (free and not visited).

iv. If the goal is found, the search stops, and the path is saved.


3. Tracking Path & Traversal Order:
   
i. The order in which cells are visited is recorded.

ii. If a path to the goal is found, it is displayed along with the number of steps.

iii. The order of visited cells (topological order) is shown to understand how the search worked.


# Output:

<img width="501" alt="image" src="https://github.com/user-attachments/assets/a16164dd-0c80-49ef-a56f-a66b28e0f7df" />
