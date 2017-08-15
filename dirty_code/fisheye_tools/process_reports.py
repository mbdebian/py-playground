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
    grouped_result = []
    with open(__args.input_file) as f:
        csvreader = csv.reader(f, delimiter=',', quotechar='"')
        last_seen_date = None
        last_seen_date_commit_set = set()
        last_seen_date_commit_comment = None
        for i, entry in enumerate(csvreader):
            if i == 0:
                # Header
                grouped_result.append(entry)
            else:
                # Change the date format to stop at 'day' resolution
                current_entry_date = entry[CSV_COLUMN_NUMBER_DATE].split(' ')[0]
                if not last_seen_date:
                    last_seen_date = current_entry_date
                    last_seen_date_commit_comment = entry[CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                    last_seen_date_commit_set.add(entry[CSV_COLUMN_NUMBER_COMMIT_ID])
                    # In this case, the author is the same for all the listing

if __name__ == '__main__':
    main()
