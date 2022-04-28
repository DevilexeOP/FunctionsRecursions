from itertools import product


def factorial_iter(n):
    n = 13
    product = 1 
    for i in range(n):
        product = product * (i + 1)
        return product
    f = factorial_iter(13)
    print(factorial_iter)
