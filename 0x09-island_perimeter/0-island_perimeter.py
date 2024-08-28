#!/usr/bin/python3
"""
Module that calculates the perimeter of an island
"""

def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island.
    
    :param grid: List of list of integers representing the grid.
    :return: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i-1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1
    return perimeter
