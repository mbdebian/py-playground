# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 10-10-2017 13:40
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Playground for algorithms and data structures
"""

from bisect import bisect_left
from collections import deque, defaultdict
from heapq import heappush, heappop, nsmallest

# Double-ended Queue
print("[--- FIFO example ---]")
fifo = deque()
fifo.append(1)      # Producer
x = fifo.popleft()  # Consumer
print("[{}]".format("-" * 20))

# Example of default dictionary
print("[--- defaultdict example ---]")
stats = defaultdict(int)
stats['my_counter'] += 1
print("[{}]".format("-" * 20))

# Example of Heap Queue
print("[--- Heap Queue example ---]")
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3
print(heappop(a), heappop(a), heappop(a), heappop(a))
print("[{}]".format("-" * 20))

# Example of bisect
print("[--- Bisect example ---]")
x = list(range(10**6))
i = x.index(991234)
i = bisect_left(x, 991234)
print("[{}]".format("-" * 20))
