# 0x05. N Queens

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Example](#example)
- [Resources](#resources)
- [Author](#author)

## Description

The **N Queens** puzzle is a classic problem in computer science and mathematics. The goal is to place N queens on an N×N chessboard in such a way that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

In this project, you will be implementing a solution to the N Queens problem using the **backtracking algorithm**. The program will accept a single argument, **N**, which represents the size of the board and the number of queens to be placed. The output should include all possible solutions to the problem, each solution being represented as a list of lists. Each list will contain two integers, where the first integer is the row index and the second integer is the column index.

## Requirements

- **Python Version:** Python 3.x (interpreted/compiled on Ubuntu 20.04 LTS).
- **PEP 8:** Code must conform to the PEP 8 style guide.
- **Execution:** All files should be executable.
- **Shebang:** The first line of all your files should be exactly `#!/usr/bin/python3`.
- **Imports:** Only the `sys` module is allowed.

## Usage

To run the program, use the following command:

```bash
./0-nqueens.py N
```

- **N:** The size of the board and the number of queens. Must be an integer greater than or equal to 4.

### Error Handling

- If the user provides the wrong number of arguments:
  - Print `Usage: nqueens N` followed by a new line.
  - Exit with status code `1`.
- If `N` is not an integer:
  - Print `N must be a number` followed by a new line.
  - Exit with status code `1`.
- If `N` is less than `4`:
  - Print `N must be at least 4` followed by a new line.
  - Exit with status code `1`.

## Algorithm

The solution to the N Queens problem involves **backtracking**:

1. **Initialization:**
   - Start with an empty board.
   
2. **Placement:**
   - Place a queen on the board row by row.
   - After placing a queen, recursively attempt to place the next queen in a subsequent row.
   
3. **Backtrack:**
   - If placing the next queen is impossible (due to threats), backtrack to the previous row and move the queen to a new position.
   - Continue this process until all queens are placed on the board without threats.

4. **Output:**
   - Print each valid solution as a list of lists.

## Example

Here’s an example of how the program should work:

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Resources

- [Backtracking Algorithms](https://en.wikipedia.org/wiki/Backtracking)
- [Recursion in Python](https://docs.python.org/3.8/tutorial/controlflow.html#recursive-functions)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)
