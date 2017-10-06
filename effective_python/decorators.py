# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 06-10-2017 6:22
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Playground for decorators in Python
"""


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{}({},{}) -> {}".format(func.__name__, args, kwargs, result))
        return result

    return wrapper


def fibonacci(n):
    """
    Return the n-th Fibonacci number
    :param n: n-th fibonacci number requested
    :return: the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)
