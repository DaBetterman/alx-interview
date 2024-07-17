#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables to keep track of total file size and status code counts
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
line_count = 0


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) to print stats before exiting.
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """
    Print the total file size and counts of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


# Set up the signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        # Regex to match the log format
        match = re.match(
            r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$', line.strip()
            )
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code in status_counts:
                status_counts[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    pass
finally:
    # Print final stats when the script ends
    print_stats()
