import numpy as np

rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")

matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])

A = np.array(matrix_entries, dtype=np.float64)

n = rows  # Number of rows, assuming square matrix for power method

num_iterations = int(input("Enter the number of iterations for the power method: "))
x = np.ones((n, 1), dtype=np.float64)  # Initial guess for eigenvector

for _ in range(num_iterations):
    x_new = np.dot(A, x)
    norm = np.linalg.norm(x_new)
    if norm == 0:
        print("The vector became zero. Power method cannot proceed.")
        break
    x = x_new / norm

Ax = np.dot(A, x)
# The numerator and denominator must be scalars for float(). Use flatten or extract 0-d scalars:
numerator = (x.T @ Ax).item()
denominator = (x.T @ x).item()
dominant_eigenvalue = numerator / denominator

print("Dominant Eigenvalue (approx.):", dominant_eigenvalue)
print("Corresponding Eigenvector (approx.):")
print(x)

     
