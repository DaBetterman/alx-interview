#!/usr/bin/python3
"""
Module to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Module to rotate a 2D matrix 90 degrees clockwise.
    """

    new = len(matrix)

    for i in range(new):
        for j in range(i, new):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(new):
        matrix[i].reverse()
