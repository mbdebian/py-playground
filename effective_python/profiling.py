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
