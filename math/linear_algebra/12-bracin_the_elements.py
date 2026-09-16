#!/usr/bin/env python3
"""Module that performs element-wise operations on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Return the element-wise sum, difference, product and quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
