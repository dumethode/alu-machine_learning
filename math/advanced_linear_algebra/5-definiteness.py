#!/usr/bin/env python3
"""Module that calculates the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Return the definiteness of matrix as a string, or None."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2:
        return None
    if matrix.shape[0] == 0 or matrix.shape[0] != matrix.shape[1]:
        return None
    if not np.array_equal(matrix, matrix.T):
        return None
    values = np.linalg.eigvals(matrix)
    if np.all(values > 0):
        return "Positive definite"
    if np.all(values >= 0):
        return "Positive semi-definite"
    if np.all(values < 0):
        return "Negative definite"
    if np.all(values <= 0):
        return "Negative semi-definite"
    return "Indefinite"
