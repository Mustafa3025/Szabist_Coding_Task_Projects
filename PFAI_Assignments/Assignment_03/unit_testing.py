import ai_matrix_ops as ops
import numpy as np


if __name__ == '__main__':

    matrix_1 = np.array([[1, 2], [3, 4]])
    matrix_2 = np.array([[4, 3], [2, 1]])
    
    print(f'Matrix Multiplication : {ops.matrix_multiply(matrix_1, matrix_2)}')
    print()
    
    print(f'Matrix Inversion : {ops.matrix_inversion(matrix_1)}')
    print()
    
    print(f'Matrix Determinant : {ops.matrix_determinant(matrix_1)}')
    print()
    
    matrix_A = np.array([[5, 6], [7, 8]])
    matrix_B = np.array([1, 2])
    
    print(f'Matrix Linear System Solver : {ops.linear_system_Solver(matrix_A, matrix_B)}')
    print()
    
    print(f'Matrix Eigen Values : {ops.matrix_eigenvalues(matrix_1)}')
    print()
    
    print(f'Matrix Decomposition : {ops.matrix_decomposition(matrix_1)}')
    print()
    
    print(f'Matrix Rank : {ops.matrix_rank(matrix_1)}')
    print()
    
    print(f'Matrix Norm Calculation 1-Norm : {ops.matrix_norm_calculation_1_norm(matrix_1)}')
    print()
    
    
    print(f'Matrix Norm Calculation 2-Norm : {ops.matrix_norm_calculation_2_norm(matrix_1)}')
    print()