import numpy as np

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

result = np.matmul(a1, b1)  # Using .matmul() for matrix multiplication
print(result)

# OR:
print()
print(a1 @ b1)