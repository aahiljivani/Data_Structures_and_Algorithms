# ELLMatrix Class Documentation

## Overview

The `ELLMatrix` class is designed to efficiently store and manipulate sparse matrices using the ELLPACK format. This format is particularly useful for matrices with a large number of zeros, allowing for significant memory savings and potentially faster computation for certain operations.

## Features

- **Initialization from a dense matrix:** Convert a regular 2D list (dense matrix) into the compressed ELLPACK format.
- **Compression:** Internally represents the matrix in a compressed format that only stores non-zero elements and their column indices.
- **Reconstruction:** Ability to reconstruct the original dense matrix from the compressed format.

## Usage

### Initialization

To initialize an `ELLMatrix` object, you need to provide a dense matrix (2D list) as input. The dense matrix should be in a row-major format.

Example:
```python
dense_matrix = [
    [0, 0, 3, 0, 4],
    [0, 2, 0, 3, 0],
    [1, 0, 0, 0, 0],
]

ell_matrix = ELLMatrix(dense_matrix)
