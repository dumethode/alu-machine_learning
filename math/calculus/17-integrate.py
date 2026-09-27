#!/usr/bin/env python3
"""Module for calculating the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial."""
    if type(poly) is not list or len(poly) == 0:
        return None
    for i in poly:
        if type(i) not in (int, float):
            return None
    if type(C) is not int:
        return None
    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef.is_integer():
            coef = int(coef)
        integral.append(coef)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
