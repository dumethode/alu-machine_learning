#!/usr/bin/env python3
"""Module for Binomial distribution."""


class Binomial:
    """Class that represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p_calc = 1 - (variance / mean)
            n_calc = round(mean / p_calc)
            self.n = n_calc
            self.p = mean / self.n

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        
        def factorial(num):
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return fact
            
        comb = factorial(self.n) / (factorial(k) * factorial(self.n - k))
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes."""
        k = int(k)
        if k < 0:
            return 0
        cdf_val = 0
        for i in range(k + 1):
            cdf_val += self.pmf(i)
        return cdf_val
