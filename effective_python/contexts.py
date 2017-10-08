# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 08-10-2017 6:50
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Playing with contextlib and locks
"""

import logging


# Logging example
def my_function():
    logging.debug("Some debug data")
    logging.error("Error log here")
    logging.debug("More debug data")

# Call
my_function()