# N Queens Solver

This Python module provides functionality to solve the N Queens problem. The N Queens problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. Here's a detailed breakdown of how the module works:

## Functions

`solve_queens(n)`

This function solves the N Queens problem for a given board size n.

**Arguments:**

    n (int): The size of the chessboard (n×n) and the number of queens to place.

**Returns:**

    list of list of list of bool: Returns a list of solutions, where each solution is a list representing the board state, and each board state is a list of lists containing booleans indicating queen positions.

**How it works:**

1. Initializes sets to keep track of columns and diagonals that are under attack.
2. Creates a results list to store all valid board configurations.
3. Initializes a board with False values, indicating no queens placed.
4. Defines a recursive backtrack function to place queens row by row:
    - If r equals n, a solution is found and added to results.
    - For each column in the current row, checks if placing a queen is safe.
    - If safe, updates the board and sets, then recursively attempts to place queens in the next row.
    - After the recursive call, removes the queen and updates the sets to backtrack.
5. Calls the backtrack function starting from row 0. 
6. Returns the list of results.

`transform_boolean_matrix(matrix)`

This helper function transforms a boolean matrix representing a chessboard into a list of row-column pairs where queens are placed.

**Arguments:**

    matrix (list of list of bool): A list of lists representing the chessboard, with True indicating a queen's position.

**Returns:**

    list of list of int: Returns a list of row-column pairs indicating the positions of queens.

**How it works:**

    Iterates over each row and column of the matrix.
    If a queen (True) is found, appends its [row_index, col_index] pair to the result list.
    Returns the result list.


## How to Run
1. Save the script to a file, e.g., n_queens.py.
2. Run the script from the command line, providing the board size as an argument:

       [bash]
       ./0-nqueens.py n # where n is an argument to solve with n queens (e.g. 8)
3. The script will output each solution as a list of row-column pairs where queens are placed.
