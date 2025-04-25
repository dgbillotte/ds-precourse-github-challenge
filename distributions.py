import math


def binomial_pmf(n, p, k):
    if k < 0 or k > n:
        return 0
    comb = math.comb(n, k)  # or use factorial(n) / (factorial(k) * factorial(n-k))
    return comb * (p ** k) * ((1 - p) ** (n - k))


def poisson_pmf(k, lam):
    if k < 0:
        return 0
    return (math.exp(-lam) * (lam ** k)) / math.factorial(k)


def geometric_pmf(n, p):
    if n < 1 or not (0 < p <= 1):
        return 0
    return ((1 - p) ** (n - 1)) * p
