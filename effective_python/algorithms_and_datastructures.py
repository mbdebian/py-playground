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

from collections import deque, defaultdict
from heapq import heappush, heappop, nsmallest

# Double-ended Queue
fifo = deque()
fifo.append(1)      # Producer
x = fifo.popleft()  # Consumer

# Example of default dictionary
stats = defaultdict(int)
stats['my_counter'] += 1

# Example of Heap Queue
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
print(heappop(a), heappop(a), heappop(a), heappop(a))