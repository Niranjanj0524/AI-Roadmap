import numpy as np

numbers = np.array([10,20,30,40])
print(numbers)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n",matrix)
print("Number of Diamesions: ", matrix.ndim)
print("Rows & Columns: ", matrix.shape)
print("Total no.of elements: ", matrix.size)
print("Data Type: ", matrix.dtype)

print("\n", np.sum(numbers))

print(np.min(numbers))
print(np.max(numbers))