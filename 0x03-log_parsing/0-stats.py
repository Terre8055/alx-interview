#!/usr/bin/env python3
"""Module to parse log files into stdout"""

import sys


def parse_line(line):
    """Helper method to parse line from stdin"""


    try:
        parts = line.split(' ')
        if len(parts) != 10:
            return None

        status_code = int(parts[8])
        if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
            return None

        file_size = int(parts[9])
        return status_code, file_size
    except ValueError:
        return None

def print_statistics(total_file_size, status_counts):
	"""Helper method to print statements"""


    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_counts.keys()):
        print(f'{status_code}: {status_counts[status_code]}')

def main():
	"""Starting method in program"""


    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_data = parse_line(line)
            if parsed_data is None:
                continue

            status_code, file_size = parsed_data
            total_file_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass

    # Print final statistics
    print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
