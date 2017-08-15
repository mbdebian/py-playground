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
INPUT_CSV_COLUMN_NUMBER_COMMIT_ID = 0
INPUT_CSV_COLUMN_NUMBER_DATE = 1
INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT = 2
INPUT_CSV_COLUMN_NUMBER_CHANGED_PATH = 3

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


class ResultObject:
    def __init__(self):
        self.date = ""
        self.author = ""
        self.no_commits = ""
        self.repo_name = ""
        self.commit_details = ""

    @staticmethod
    def get_csv_header():
        return [
            'Date',
            'Author',
            'Number of Commits',
            'Repository',
            'Commit Details'
        ]

    def get_csv_entry(self):
        return [
            self.date,
            self.author,
            self.no_commits,
            self.repo_name,
            self.commit_details
        ]


def main():
    app_bootstrap()
    __logger.info("Input file '{}'".format(__args.input_file))
    # We assume the data is already sorted by date
    grouped_result = []
    output_file = __args.input_file[:__args.input_file.rfind('.')] + "-date_grouped_report.csv"
    with open(__args.input_file) as f:
        with open(output_file, 'w') as wf:
            csvreader = csv.reader(f, delimiter=',', quotechar='"')
            last_seen_date = None
            last_seen_date_commit_set = set()
            last_seen_date_commit_comment = None
            for i, entry in enumerate(csvreader):
                if i == 0:
                    # Result differs from input, so we just skip the header
                    pass
                else:
                    # Change the date format to stop at 'day' resolution
                    current_entry_date = entry[INPUT_CSV_COLUMN_NUMBER_DATE].split(' ')[0]
                    if not last_seen_date:
                        last_seen_date = current_entry_date
                        last_seen_date_commit_comment = entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                        last_seen_date_commit_set.add(entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_ID])
                        # In this case, the author is the same for all the listing
                    else:
                        if current_entry_date == last_seen_date:
                            # Group entry
                            # Add the commit ID
                            last_seen_date_commit_set.add(entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_ID])
                            # If our current commit comment is empty and this entry has a useful one, replace it
                            if len(last_seen_date_commit_comment) == 0:
                                last_seen_date_commit_comment = entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                        else:
                            # Start another entry group
                            pass


if __name__ == '__main__':
    main()
