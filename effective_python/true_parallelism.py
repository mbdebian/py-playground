# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 05-10-2017 9:28
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Experimenting with parallelism in python
"""


def greatest_common_divisor(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
