# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 10-10-2017 13:27
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Playground for memory management and leaks
"""

import gc

found_objects = gc.get_objects()
print("{} objects before".format(len(found_objects)))
