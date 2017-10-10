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

from collections import deque

# Double-ended Queue
fifo = deque()
fifo.append(1)      # Producer
x = fifo.popleft()  # Consumer
