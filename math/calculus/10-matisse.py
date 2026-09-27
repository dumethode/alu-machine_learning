#!/usr/bin/env python3
"""Module for calculating the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial."""
    if type(poly) is not list or len(poly) == 0:
        return None
    for i in poly:
        if type(i) not in (int, float):
            return None
    if len(poly) == 1:
        return [0]
    derivative = [poly[i] * i for i in range(1, len(poly))]
    if all(x == 0 for x in derivative):
        return [0]
    return derivative
