# TITLE OF THE PROBLEM : 
Given an undirected graph with N vertices and M edges. My task is to implement a Python program that uses Backtracking to determine whether the graph can be colored using K colors such that no two adjacent vertices share the same color. The input will be read from a file, where the first line contains three integers: N (number of vertices, numbered from 0 to N−1), M (number of edges), and K (number of available colors). Each of the following M lines contains two integers u and v, representing an undirected edge between vertex u and vertex v.

# PROCEDURE/ANALYSIS : 

1. Input Parsing:
   
i. The first line contains three integers: N (vertices), M (edges)  and K (available 
colors). 

ii. The next M lines describe the edges between vertices u and v. 


2. Graph Representation:
   
i. The graph is represented using an adjacency matrix, where graph[u][v] is 1 if 
there’s an edge, and 0 otherwise. 


3. Backtracking Algorithm:
   
i. Start with an empty color assignment (all vertices are initially uncolored). 

ii. Try different colors for each vertex, check if they are valid based on adjacent   
vertices.

iii. If a conflict occurs, backtrack and try another color. 


4. Output:
   
i. If a valid coloring is found, display the color assignment. 

ii. If no valid coloring is possible, show that it’s not possible with the given 
number of colors.


# OUTPUT :

#Input and Output For Case_01 :
![2-0](https://github.com/user-attachments/assets/d56e41c8-bcde-462a-b7d0-eefac240622d)

#Input and Output For Case_02 :
![2-1](https://github.com/user-attachments/assets/b599f51c-9d46-49d3-9f00-c561130d77b8)

