#!/usr/bin/python3
"""
Pascal's Triangle.
"""

def pascal_triangle(nums):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        nums (int): The number of rows to generate in Pascal's Triangle.
                    If nums is less than or equal to 0, returns an empty list.

    Returns:
        List[List[int]]: A list of lists, where each inner list represents
                         a row of Pascal's Triangle.
    """
    # Check if the input is less than or equal to 0
    if nums <= 0:
        return []

    # Starting with the first row
    triangle = [[1]]

    for index in range(1, nums):
        # Every row starts with 1
        row = [1]
        for element in range(1, index):
            # Each element is the sum of the two elements above it
            row.append(triangle[index - 1][element - 1] + triangle[index - 1][element])
        # Every row ends with 1
        row.append(1)
        triangle.append(row)

    return triangle
