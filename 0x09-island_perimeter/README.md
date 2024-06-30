# Island Perimeter Calculation

This Python module calculates the perimeter of an island represented in a grid. The module contains a single function, island_perimeter, which takes a grid (a list of lists of integers) as input and returns an integer indicating the perimeter of the island.

## Function

`island_perimeter(grid)`: This is the main function of the module. It calculates the perimeter of the island in the given grid.

### Parameters
`grid (list of list of int)`: A 2D grid representing the island and water. The grid contains integers where 1 represents land and 0 represents water.

### Returns

`int`: The perimeter of the island.

### Description
The function iterates over each cell in the grid. For each land cell (1), it initially considers it to have 4 sides. Then, it checks the adjacent cells (up, down, left, and right). If an adjacent cell is also land, it subtracts 1 from the perimeter count for that cell. Finally, it sums up the perimeter contributions from all land cells to get the total perimeter of the island.



## Example Usage

```
from island_perimeter_module import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print("Island Perimeter:", island_perimeter(grid))  # Output: Island Perimeter: 16

```