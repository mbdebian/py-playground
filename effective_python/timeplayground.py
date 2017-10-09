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
from datetime import datetime, timezone

# From time to local time
print("---> From time to local time")
now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

# From local time to UTC
print("---> From localtime to UTC")
time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

# Now using datetime module
now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)