#!/usr/bin/env python3
"""Module for Multivariate Normal distribution."""
import numpy as np


class MultiNormal:
    """Class that represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initializes MultiNormal distribution."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        data_dev = data - self.mean
        self.cov = np.matmul(data_dev, data_dev.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean
        sign, logdet = np.linalg.slogdet(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        
        mah_dist = np.matmul(np.matmul(diff.T, inv_cov), diff)
        
        # Using log space calculation for numerical stability and exact precision match
        exponent = -0.5 * mah_dist
        norm_const = -(d / 2) * np.log(2 * np.pi) - 0.5 * logdet
        
        return float(np.exp(norm_const + exponent))
