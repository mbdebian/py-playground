# 
# Author    : Manuel Bernal Llinares
# Project   : py-playground
# Timestamp : 10-09-2017 6:31
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Properties playground
"""

import time


class PublicPropertyExample:
    def __init__(self, mensaje):
        self.mi_mensaje = mensaje

    @property
    def mi_mensaje(self):
        return "{} - {}".format(time.time(), self.__mi_mensaje)

    @mi_mensaje.setter
    def mi_mensaje(self, mensaje):
        self.__mi_mensaje = mensaje


class PrivatePropertyExperiment:
    def __init__(self, mensaje):
        self.__mi_mensaje = mensaje

    def __str__(self):
        print(self.__mi_mensaje)


def main():
    ppe = PublicPropertyExample("Initial message")
    print(ppe.mi_mensaje)
    print("-" * 12)
    priv_ppe = PrivatePropertyExperiment("Initial Private Message")
    print(priv_ppe)


if __name__ == '__main__':
    main()
