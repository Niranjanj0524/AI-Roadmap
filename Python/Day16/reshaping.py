import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("--- 2D Indexing ---")
print("10. Print 5:", matrix[1, 1])

print("11. Print 9:", matrix[2, 2])

print("12. First row:", matrix[0, :])

print("13. Third row:", matrix[2, :])

print("14. First column:", matrix[:, 0])

print("15. Third column:", matrix[:, 2])


print("\n--- 2D Slicing ---")

print("16. Extracted sub-matrix:\n", matrix[0:2, 0:2])

print("17. First two rows:\n", matrix[:2, :])

print("18. Last two rows:\n", matrix[-2:, :])


print("\n--- Reshaping ---")
arr_12 = np.arange(1, 13)
matrix_3x4 = arr_12.reshape(3, 4)
print("19. Reshaped 3x4 matrix:\n", matrix_3x4)

flattened = matrix_3x4.flatten()
print("20. Flattened array:", flattened)