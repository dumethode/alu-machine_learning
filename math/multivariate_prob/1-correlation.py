#!/usr/bin/env python3
"""Module for calculating a correlation matrix."""
import numpy as np


def correlation(C):
    """Calculates a correlation matrix."""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std = np.expand_dims(np.sqrt(np.diagonal(C)), axis=1)
    corr = C / np.matmul(std, std.T)
    return corr
