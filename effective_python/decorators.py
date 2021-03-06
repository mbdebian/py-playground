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

import time
# @wraps decorator will take care of preserving the function metadata
from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{}({},{}) -> {}".format(func.__name__, args, kwargs, result))
        return result

    return wrapper


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("[Timing] Call '{}', {}s".format(func.__name__, (end - start)))
        return result

    return wrapper


@trace
@timing
def fibonacci(n):
    """
    Return the n-th Fibonacci number
    :param n: n-th fibonacci number requested
    :return: the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# Run
print(fibonacci)
fibonacci(3)
