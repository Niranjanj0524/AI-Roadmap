import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matrix)
print()

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print("Addition of Matrix A & B: ", A + B) 
print("Substraction of Matrix A & B: ", A - B) 
print("Multiplication of Matrix A & B: ", A * B) 
print("Division of Matrix A & B: ", A / B) 

print()

print("Mean of Matrix: ", np.mean(matrix)) 
print("Max of Matrix: ", np.max(matrix)) 
print("Min of Matrix: ", np.min(matrix)) 