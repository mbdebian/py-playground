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

import io
import re
import csv
import logging
import argparse

# Constants
INPUT_CSV_COLUMN_NUMBER_COMMIT_ID = 0
INPUT_CSV_COLUMN_NUMBER_DATE = 1
INPUT_CSV_COLUMN_NUMBER_AUTHOR = 2
INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT = 3
INPUT_CSV_COLUMN_NUMBER_CHANGED_PATH = 4
# FishEye URLs
FISHEYE_URL_BASELINE_FOR_COMMIT_ID_DETAILS = 'http://fisheye.ebi.ac.uk/changelog/pride-repo?cs='
# CSV
OUTPUT_CSV_DELIMITER = ','
OUTPUT_CSV_INTERNAL_DELIMITER = ';'

# Globals
__logger = None
__args = None


# Helpers
def get_fisheye_url_for_commit_details(commit_id):
    return "{}{}".format(FISHEYE_URL_BASELINE_FOR_COMMIT_ID_DETAILS,
                         commit_id)


def clean_multiline_commit_comments(input_file, output_file):
    """
    This method cleans developers bad practices of using multiline commit comments, and fisheye bad reporting on not
    collapsing or removing their new line characters upon CSV exporting"
    :param input_file: input file to clean
    :param output_file: output clean file to produce
    :return: no returned value
    """
    with open(input_file) as f:
        with open(output_file, 'w') as wf:
            clean_state = True
            for input_line in f:
                if clean_state:
                    if input_line.endswith("\"\n"):
                        wf.write(input_line)
                    else:
                        wf.write(input_line.strip() + " ")
                        clean_state = False
                else:
                    if input_line.endswith("\"\n"):
                        wf.write(input_line)
                        clean_state = True
                    else:
                        wf.write(input_line.strip() + " ")


def clean_even_more_rubbish_commit_comments(input_file, output_file):
    commit_entry_re = r"^\"\d+\","
    with open(input_file) as f:
        with open(output_file, 'w') as wf:
            buffer = ""
            for i, input_line in enumerate(f):
                if i == 0:
                    buffer = input_line.strip()
                    continue
                if re.match(commit_entry_re, input_line):
                    # Flush the buffer to file and put this on it
                    # The removal of double quotes is just for a particular use case on a report I have to prepare
                    wf.write(buffer.replace('""', '') + "\n")
                    buffer = input_line.strip()
                else:
                    # Append to the buffer
                    buffer = buffer + " " + input_line.strip()
            # Flush the last buffer content
            wf.write(buffer + "\n")


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
        qualifier = "commit"
        if int(self.no_commits) > 1:
            qualifier = "commits"
        return [
            self.date,
            self.author,
            "{} {}".format(self.no_commits, qualifier),
            self.repo_name,
            self.commit_details
        ]


def main():
    app_bootstrap()
    __logger.info("Input file '{}'".format(__args.input_file))
    # We assume the data is already sorted by date
    grouped_result = []
    input_file_name = __args.input_file[:__args.input_file.rfind('.')]
    cleaned_file = input_file_name + "-cleaned.csv"
    output_file = input_file_name + "-date_grouped_report.csv"
    clean_even_more_rubbish_commit_comments(__args.input_file, cleaned_file)
    with open(cleaned_file) as f:
        with open(output_file, 'w') as wf:
            csvreader = csv.reader(f, delimiter=',', quotechar='"')
            csvwriter = csv.writer(wf, delimiter=OUTPUT_CSV_DELIMITER, quotechar='"')
            # Write output report header
            csvwriter.writerow(ResultObject.get_csv_header())
            last_seen_date = None
            last_seen_date_commit_set = set()
            last_seen_date_commit_comment = None
            last_seen_date_author = None
            last_seen_date_repo_names = set()
            for i, entry in enumerate(csvreader):
                if i != 0:
                    # Result differs from input, so we just skip the header
                    # Change the date format to stop at 'day' resolution
                    #__logger.debug("[Entry {:03}] '{}'".format(i, str(entry)))
                    current_entry_date = entry[INPUT_CSV_COLUMN_NUMBER_DATE].split(' ')[0]
                    if not last_seen_date:
                        last_seen_date = current_entry_date
                        last_seen_date_commit_comment = entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                        last_seen_date_commit_set.add(entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_ID])
                        last_seen_date_author = entry[INPUT_CSV_COLUMN_NUMBER_AUTHOR]
                        entry_path = entry[INPUT_CSV_COLUMN_NUMBER_CHANGED_PATH]
                        last_seen_date_repo_names.add(entry_path[:entry_path.find('/')])
                        # In this case, the author is the same for all the listing
                    else:
                        if current_entry_date == last_seen_date:
                            # Group entry
                            # Add the commit ID
                            last_seen_date_commit_set.add(entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_ID])
                            # Add the repo name, because multiple repos could have been committed on the same day
                            entry_path = entry[INPUT_CSV_COLUMN_NUMBER_CHANGED_PATH]
                            last_seen_date_repo_names.add(entry_path[:entry_path.find('/')])
                            # If our current commit comment is empty and this entry has a useful one, replace it
                            if len(last_seen_date_commit_comment) == 0:
                                last_seen_date_commit_comment = entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                        else:
                            # Start another entry group
                            result_entry = ResultObject()
                            result_entry.date = last_seen_date
                            result_entry.author = last_seen_date_author
                            result_entry.no_commits = len(last_seen_date_commit_set)
                            result_entry.repo_name = ",".join([repo_name for repo_name in last_seen_date_repo_names])
                            # Produce the URLs for the commit details
                            result_entry.commit_details = ", ".join(
                                [get_fisheye_url_for_commit_details(commit_id)
                                 for commit_id
                                 in last_seen_date_commit_set])
                            # Write entry to output report
                            csvwriter.writerow(result_entry.get_csv_entry())
                            # Fill in the tracking information for the current entry
                            last_seen_date = current_entry_date
                            last_seen_date_commit_comment = entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_COMMENT]
                            last_seen_date_commit_set = {entry[INPUT_CSV_COLUMN_NUMBER_COMMIT_ID]}
                            last_seen_date_author = entry[INPUT_CSV_COLUMN_NUMBER_AUTHOR]
                            entry_path = entry[INPUT_CSV_COLUMN_NUMBER_CHANGED_PATH]
                            last_seen_date_repo_names = {entry_path[:entry_path.find('/')]}
            # Flush possible last entry
            if last_seen_date:
                result_entry = ResultObject()
                result_entry.date = last_seen_date
                result_entry.author = last_seen_date_author
                result_entry.no_commits = len(last_seen_date_commit_set)
                result_entry.repo_name = ",".join([repo_name for repo_name in last_seen_date_repo_names])
                # Produce the URLs for the commit details
                result_entry.commit_details = ", ".join(
                    [get_fisheye_url_for_commit_details(commit_id)
                     for commit_id
                     in last_seen_date_commit_set])
                # Write entry to output report
                csvwriter.writerow(result_entry.get_csv_entry())


if __name__ == '__main__':
    main()
