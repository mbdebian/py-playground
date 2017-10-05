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

import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def greatest_common_divisor(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# Running this function in serials
print("[{} Serial Run {}]".format("-" * 20, "-" * 20))
numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]
start = time.time()
results = list(map(greatest_common_divisor, numbers))
end = time.time()
print("[---> It took {:.3} seconds <---]".format(end - start))
# Now in parallel
print("[{} PARALLEL Run (ThreadPoolExecutor) {}]".format("-" * 20, "-" * 20))
start = time.time()
pool = ThreadPoolExecutor(max_workers=os.cpu_count())
results = list(pool.map(greatest_common_divisor, numbers))
end = time.time()
print("[---> It took {:.3} seconds <---]".format(end - start))
# Using ProcessPoolExecutor
print("[{} PARALLEL Run (ProcessPoolExecutor) {}]".format("-" * 20, "-" * 20))
start = time.time()
pool = ProcessPoolExecutor(max_workers=os.cpu_count())
results = list(pool.map(greatest_common_divisor, numbers))
end = time.time()
print("[---> It took {:.3} seconds <---]".format(end - start))