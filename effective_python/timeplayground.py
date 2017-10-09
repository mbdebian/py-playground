# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 09-10-2017 9:17
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Playing with time and datetime
"""

from time import localtime, strftime, mktime, strptime

# From time to local time
now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

# From local time to UTC