# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 10-10-2017 12:42
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
This module is for playing with profiling applications in python
"""

from pstats import Stats
from random import randint
from cProfile import Profile


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


max_size = 10 ** 4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

# Run the call with a profiler
profiler = Profile()
profiler.runcall(test)

