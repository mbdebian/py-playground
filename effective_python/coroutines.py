# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 05-10-2017 8:41
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Coroutines example from the book
"""


def my_coroutine():
    while True:
        received = yield
        print('Received: ', received)


it = my_coroutine()
next(it)  # Prime the coroutine
it.send('First')
it.send('Second')
