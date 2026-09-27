#!/usr/bin/env python3
"""
Module for calculating the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    
    Args:
        poly (list): A list of coefficients representing a polynomial.
        C (int): An integer representing the integration constant.
        
    Returns:
        list: A new list of coefficients representing the integral.
        None: If poly or C are not valid.
    """
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
        # Convert to int if the coefficient is a whole number
        if coef.is_integer():
            coef = int(coef)
        integral.append(coef)

    # Strip trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
