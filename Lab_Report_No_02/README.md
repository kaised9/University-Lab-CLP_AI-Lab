# TITLE OF THE PROBLEM :

Given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). My task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell.I may move up, down, left, or right to adjacent empty cells, but I cannot pass through walls and each cell may be visited only once during a single path exploration.

# PRODEDURE/ANALYSIS 

1. Problem Understanding:
   
i.  A grid is given where 0 represents empty spaces and 1 represents walls.

ii. The goal is to check if there is a path from a start point to a target point. 

iii. We can only move to adjacent cells (up, down, left, or right), and you can’t  
move through walls. 



2. IDDFS Algorithm Steps:

i.  Start by reading the grid size and its content (rows and columns). 

ii. Read the start and target positions.

iii. Implement the IDDFS algorithm using a Depth-Limited Search (DLS)     
function. 

iv. Increase the depth limit iteratively and explore paths. 

v.  Keep track of the path traversal. 

# OUTPUT : 

#Case_01 : Input & OutPut
![1-0](https://github.com/user-attachments/assets/2e7ff4bd-9918-4b8f-ae0c-f73db3853b14)

#Case_02 : Input & OutPut
![1-1](https://github.com/user-attachments/assets/cac19f53-30a7-4eff-81f6-4c2e34847268)
