Problem: Implement a modified K-Means clustering algorithm using Python. In this task, you must generate a data file containing 100 Cartesian points P(x, y) and 10 initial cluster centers C(x, y). The algorithm should be rewritten to use the Manhattan distance method for calculating distances between points and clusters. Additionally, you are required to create a 2D visualization of the clustered data using a matrix, where each cell represents a coordinate on the plane and displays either a data point or a cluster center using distinct symbols. This visualization must be displayed using only the print() function.

PROCEDURE/ANALYSIS: 
Steps are given in below : 
1. Data Generation:
a. A grid of size 11x11 (121 total coordinates) was used.

b. Randomly selected 100 unique points from the grid as input data.

c. Generated 10 random cluster centers (can include overlap).

3. Distance Calculation:
   a. Manhattan distance was used to calculate the distance between each point and    
      every cluster center.
   b. Formula used :  abs(x1 - x2) + abs(y1 - y2).
   
4. K-Means Logic:
   a. Each point is assigned to the nearest cluster center using Manhattan distance.
   b. For each cluster, I find the average position of all the points in that cluster.
   c. The cluster center is moved to this new average position.
   d. This process was repeated until the cluster centers stopped changing.

5. 2D Matrix Visualization:
   a. A matrix (grid) was created to represent the points and cluster centers.
   b. Data points were marked with numbers (0-9 based on cluster ID).
   c. Cluster centers were marked with capital letters (A-J).
   d. The matrix was displayed using only print().


Output: 
![Screenshot 2025-04-25 150656](https://github.com/user-attachments/assets/a692830c-abdc-4622-a1cf-78a419a1dea9)
