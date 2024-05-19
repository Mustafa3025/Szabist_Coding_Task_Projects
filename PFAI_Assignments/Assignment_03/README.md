
---

# Linear Algebra Functions Library

This library provides various functions for performing common linear algebra operations using NumPy and its linear algebra module (`numpy.linalg`).

## Functions

### 1. `matrix_multiply(matrix_1, matrix_2)`

This function computes the matrix product of two input matrices.

- **Parameters**:
    - `matrix_1`: First input matrix.
    - `matrix_2`: Second input matrix.

- **Return Value**:
    - Returns the result of the matrix multiplication.

### 2. `matrix_inversion(matrix)`

This function computes the inverse of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix to be inverted.

- **Return Value**:
    - Returns the inverse of the input matrix.

### 3. `matrix_determinant(matrix)`

This function calculates the determinant of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns the determinant of the input matrix.

### 4. `linear_system_Solver(matrix_A, matrix_B)`

This function solves a system of linear equations represented by matrices `matrix_A` and `matrix_B`.

- **Parameters**:
    - `matrix_A`: Coefficient matrix.
    - `matrix_B`: Constant matrix.

- **Return Value**:
    - Returns the solution vector.

### 5. `matrix_eigenvalues(matrix)`

This function computes the eigenvalues of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns an array containing the eigenvalues.

### 6. `matrix_decomposition(matrix)`

This function performs Singular Value Decomposition (SVD) on the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns the singular value decomposition of the input matrix.

### 7. `matrix_rank(matrix)`

This function computes the rank of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns the rank of the input matrix.

### 8. `matrix_norm_calculation_1_norm(matrix)`

This function calculates the 1-norm (maximum absolute column sum) of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns the 1-norm of the input matrix.

### 9. `matrix_norm_calculation_2_norm(matrix)`

This function calculates the 2-norm (largest singular value) of the input matrix.

- **Parameters**:
    - `matrix`: Input matrix.

- **Return Value**:
    - Returns the 2-norm of the input matrix.

## Installation

To use this library, make sure you have NumPy installed. You can install NumPy using pip:


---
