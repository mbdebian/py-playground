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
from contextlib import contextmanager


# Logging example
def my_function():
    logging.debug("Some debug data")
    logging.error("Error log here")
    logging.debug("More debug data")


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


# Call
my_function()

# Call again using the context manager
with debug_logging(logging.DEBUG):
    print("---> Inside:")
    my_function()
print("---> After:")
my_function()

# Using the new context manager
with log_level(logging.DEBUG, 'my_log') as logger:
    logger.debug("This is my message")
    logging.debug("This will not print")
