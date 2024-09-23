#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check if the land has neighboring land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check the upper cell
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check the left cell
                    perimeter -= 2
    return perimeter
