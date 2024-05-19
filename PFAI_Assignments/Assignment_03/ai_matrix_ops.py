import numpy as np
from numpy import linalg as lin

def matrix_multiply(matrix_1, matrix_2):
    return np.matmul(matrix_1, matrix_2)

def matrix_inversion(matrix):
    return lin.inv(matrix)

def matrix_determinant(matrix):
    return lin.det(matrix)

def linear_system_Solver(matrix_A, matrix_B):
    return lin.solve(matrix_A, matrix_B)

def matrix_eigenvalues(matrix):
    return lin.eigvals(matrix)

def matrix_decomposition(matrix):
    return lin.svd(matrix)

def matrix_rank(matrix):
    return lin.matrix_rank(matrix)

def matrix_norm_calculation_1_norm(matrix):
    return np.max(np.sum(np.abs(matrix), axis = 0))

def matrix_norm_calculation_2_norm(matrix):
    return np.max(lin.svd(matrix)[1])

