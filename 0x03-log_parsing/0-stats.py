#!/usr/bin/python3
import sys
import signal
import re

# Initialize the total file size and the dictionary to count status codes
total_size = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats():
    """
    Prints the total file size and the
    count of each status code in ascending order.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """
    Signal handler for SIGINT (Ctrl+C). Prints statistics before exiting.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'(\S+) - \[(.+?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if not match:
            continue

        ip, date, status, size = match.groups()

        try:
            file_size = int(size)
            total_size += file_size
        except ValueError:
            continue

        if status in status_counts:
            status_counts[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
