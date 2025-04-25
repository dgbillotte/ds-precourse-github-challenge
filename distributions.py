import math


def binomial_pmf(n, p, k):
    if k < 0 or k > n:
        return 0
    comb = math.comb(n, k)  # or use factorial(n) / (factorial(k) * factorial(n-k))
    return comb * (p ** k) * ((1 - p) ** (n - k))


def poisson_pmf(k, lam):
    pass


def geometric_pmf(n, p):
    pass
