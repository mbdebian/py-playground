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


# Constants
CSV_COLUMN_NUMBER_COMMIT_ID = 0
CSV_COLUMN_NUMBER_DATE = 1
CSV_COLUMN_NUMBER_COMMIT_COMMENT = 2
CSV_COLUMN_NUMBER_CHANGED_PATH = 3

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
    # We assume the data is already sorted by date
    with open(__args.input_file) as f:
        input_data = csv.reader(f, delimiter=',', quotechar='"')
        __logger.info("{} entries read".format(len(input_data)))

if __name__ == '__main__':
    main()
