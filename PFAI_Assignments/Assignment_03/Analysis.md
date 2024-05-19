
---


### 1. Compressed Image
- **Purpose**: The purpose of this operation is to compress the image matrix by reducing its dimensions while preserving important information.
- **Approach**: SVD is performed on the image matrix, and the singular value matrix and left and right singular vectors are truncated to retain only a subset of singular values and vectors. The compressed image is reconstructed using the truncated matrices.
- **Implementation**: This is achieved by using the `matrix_decomposition` function to obtain the singular value decomposition of the image matrix, and then performing matrix multiplication operations to reconstruct the compressed image.

### 2. Pseudo-Inverse Matrix
- **Purpose**: Calculating the pseudo-inverse of the image matrix is useful for various image processing tasks, such as image restoration and solving linear least squares problems.
- **Approach**: The pseudo-inverse is obtained by taking the reciprocal of non-zero singular values and performing matrix multiplication operations on the truncated singular vectors and singular value matrix.
- **Implementation**: This operation involves using the `matrix_decomposition` function to obtain the SVD of the image matrix and then performing matrix multiplication operations to compute the pseudo-inverse.

### 3. Image Determinant
- **Purpose**: Calculating the determinant of the image matrix provides information about the volume scaling factor of the linear transformation represented by the matrix.
- **Approach**: The determinant of the image matrix is directly computed using the `matrix_determinant` function.
- **Implementation**: This operation involves calling the `matrix_determinant` function with the image matrix as input.

### 4. Optimal Threshold for Compression
- **Purpose**: Determining the optimal threshold for compression is crucial for balancing between image quality and compression ratio.
- **Approach**: The optimal threshold is set as half of the rank of the image matrix.
- **Implementation**: This operation involves calling the `matrix_rank` function to determine the rank of the image matrix and then computing the optimal threshold.

### 5. Singular Values and Image Rank
- **Purpose**: Obtaining the singular values and rank of the image matrix provides insights into its structure and properties.
- **Approach**: The singular values are obtained using the `matrix_decomposition` function, and the rank is determined using the `matrix_rank` function.
- **Implementation**: These operations involve calling the `matrix_decomposition` and `matrix_rank` functions with the image matrix as input.

### 6. Image Norm
- **Purpose**: Calculating the norm of the image matrix helps in quantifying its magnitude and behavior under compression.
- **Approach**: The 2-norm (largest singular value) of the image matrix is computed.
- **Implementation**: This operation involves calling the `matrix_norm_calculation_2_norm` function with the image matrix as input.

--- 
