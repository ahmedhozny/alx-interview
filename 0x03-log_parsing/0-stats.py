#!/usr/bin/python3
"""
reads input log lines from stdin, parses them according to a
specified format, and computes metrics such as total file size
and counts of HTTP status codes.
It prints these statistics after every 10 lines of input or upon receiving
a keyboard interruption (CTRL + C).
"""

import sys
import re


def print_statistics(total_file_size, status_counts):
    """
    prints statistics after every 10 lines of input or upon receiving
    """
    print("File size: {:d}".format(total_file_size))
    for k, v in sorted(status_counts.items()):
        if v > 0:
            print("{}: {}".format(k, v))


def extract_line(line):
    """
    Extracts features from input line
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )

    regex = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])

    res = re.fullmatch(regex, line)
    if res is not None:
        return res.group('status_code'), int(res.group('file_size'))
    else:
        return 0, 0


def run(status_codes):
    """
    Starts the log parsing process
    """
    status_counts = {k: 0 for k in status_codes}
    total_file_size = 0

    i = 0
    try:
        for line in sys.stdin:
            status, filesize = extract_line(line)
            if status in status_codes:
                status_counts[status], total_file_size\
                    = (status_counts[status] + 1, total_file_size + filesize)
            else:
                total_file_size += filesize
            i += 1
            if i % 10 == 0:
                print_statistics(total_file_size, status_counts)
        print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise


if __name__ == '__main__':
    status_codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    run(status_codes)
