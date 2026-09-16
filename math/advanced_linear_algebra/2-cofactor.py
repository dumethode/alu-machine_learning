#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix."""


def determinant(matrix):
    """Return the determinant of a square matrix."""
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def cofactor(matrix):
    """Return the cofactor matrix of a non-empty square matrix."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if len(row) != len(matrix) or len(row) == 0:
            raise ValueError("matrix must be a non-empty square matrix")
    n = len(matrix)
    if n == 1:
        return [[1]]
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for r in (matrix[:i] + matrix[i + 1:])]
            row.append(((-1) ** (i + j)) * determinant(sub))
        result.append(row)
    return result
