#!/usr/bin/env python3
"""Module for calculating mean and covariance."""
import numpy as np


def mean_cov(X):
    """Calculates the mean and covariance of a data set."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0, keepdims=True)
    X_dev = X - mean
    cov = np.matmul(X_dev.T, X_dev) / (n - 1)
    return mean, cov
