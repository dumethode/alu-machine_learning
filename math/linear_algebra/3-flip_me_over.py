#!/usr/bin/env python3
"""Module to transpose a 2D matrix."""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    return [[matrix[r][c] for r in range(len(matrix))]
            for c in range(len(matrix[0]))]
