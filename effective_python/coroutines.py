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


def minimize():
    print("minimize - one")
    current = yield
    print("minimize - two")
    while True:
        print("loop one")
        value = yield current
        print("loop two")
        current = min(value, current)
        print("loop three")


print("-" * 20)
# First example
it = my_coroutine()
next(it)  # Prime the coroutine
it.send('First')
it.send('Second')
print("-" * 20)
# Second example
it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
