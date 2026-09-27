#!/usr/bin/env python3
"""Module for calculating the sum of squares."""


def summation_i_squared(n):
    """Calculates the sum of i^2 from i=1 to n."""
    if type(n) is not int or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
