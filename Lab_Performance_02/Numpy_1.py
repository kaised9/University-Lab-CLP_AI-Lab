import numpy as np
c_matrix = np.random.randint(1, 101, (5, 5))

sum_of_rows = np.sum(c_matrix, axis=1)

print("Matrix Are :\n", c_matrix)
print("Row Wise Sum Are :", sum_of_rows)
