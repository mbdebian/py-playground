#!/usr/bin/env python3

#
# Author    : Manuel Bernal Llinares
# Project   : fisheye_tools
# Timestamp : 15-08-2017 10:24
# ---
# © 2017 Manuel Bernal Llinares <mbdebian@gmail.com>
# All rights reserved.
# 

"""
Sample code for processing fisheye reports
"""

import csv
import logging
import argparse

# Globals
__logger = None
__args = None


def get_cmdl():
    cmdl_version = '2017.08.15'
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='Input file in CSV format with columns '
                             '(Commit ID, Date, Author, Commit Comment, Changed Path')
    return parser.parse_args()


def app_bootstrap():
    global __logger
    global __args
    logging.basicConfig(level=logging.DEBUG)
    __logger = logging.getLogger(__name__)
    __args = get_cmdl()


def main():
    app_bootstrap()
    __logger.info("Input file '{}'".format(__args.input_file))


if __name__ == '__main__':
    main()
