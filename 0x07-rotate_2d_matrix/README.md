# Rotate 2D Matrix

## Project Overview

This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The challenge requires a good understanding of matrix manipulation and in-place operations in Python.

## Concepts Needed

### 1. Matrix Representation in Python
- Understanding how 2D matrices are represented using lists of lists in Python.
- Accessing and manipulating elements in a 2D matrix.

### 2. In-Place Operations
- Performing operations without creating a copy of the data structure.
- The importance of minimizing space usage by modifying the matrix in-place.

### 3. Matrix Transposition
- Understanding the concept of transposing a matrix (swapping rows and columns).
- Implementing matrix transposition as a step in the rotation process.

### 4. Reversing Rows in a Matrix
- How to reverse rows of a matrix by reversing their order as part of the rotation process.

### 5. Nested Loops
- Using nested loops to iterate through 2D data structures like matrices.
- Modifying elements within nested loops to achieve the desired rotation.

## Resources

### Python Official Documentation
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Nested List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)

### GeeksforGeeks Articles
- [Rotate a square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose matrix Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### Tutorialspoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

## Additional Resources

- [Mock Technical Interview](https://intranet.alxswe.com/rlt/p/1220/mock_interview.pdf)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.10)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.8.0)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Tasks

### 0. Rotate 2D Matrix
**Task:** Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

**Prototype:**
```python
def rotate_2d_matrix(matrix):
```

- **Note:** Do not return anything. The matrix must be edited **in-place**.
- You can assume the matrix will have 2 dimensions and will not be empty.

**Example:**
```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(matrix)
    print(matrix)

# Expected output:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
```
