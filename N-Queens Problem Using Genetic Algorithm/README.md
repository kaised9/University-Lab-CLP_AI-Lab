# TITLE OF THE PROBLEM : 

Solving the N-Queens Problem Using Genetic Algorithms in Python.

# PROCEDURE/ANALYSIS : 

1. Randomly create an initial population of 100 chessboards. Each board places queens randomly on the board.
   
2. Calculate the fitness of each board. Fitness checks how many queens are not attacking each other.
  
3. Select two parents based on their fitness. Boards with better fitness have a higher chance to be selected.

4. Crossover the parents to create a new child board by combining parts of both parents.
   
5. Apply mutation with a small chance to change one queen’s position randomly.
   
6. Replace the older population with new children.
   
7. Repeat the process until a perfect solution is found where no queens attack each other.
   
8. Display the final solution as a chessboard using simple print statements.


# OUTPUT : 
![Screenshot 2025-04-28 103502](https://github.com/user-attachments/assets/38a87362-e5f4-4570-bda3-7f854be276df)

![Screenshot 2025-04-28 103634](https://github.com/user-attachments/assets/13ee9b88-7455-49c1-b969-ac6a1bbac197)

![Screenshot 2025-04-28 103747](https://github.com/user-attachments/assets/3dc4f6f3-7615-45a6-bdba-318af5215779)



