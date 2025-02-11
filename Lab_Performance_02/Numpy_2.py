import numpy as np
create_Array = np.random.rand(100)

create_Array = np.random.randint(1, 1000, 100) 
Array_normalized= (create_Array - create_Array.min()) / (create_Array.max() - create_Array.min()) 

print("Original Array is :\n", create_Array)
print("\nNormalized Array is :\n", Array_normalized)
