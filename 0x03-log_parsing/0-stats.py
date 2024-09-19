#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")

def handle_exit(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_exit)

try:
    for line in sys.stdin:
        parts = line.split()
        
        if len(parts) > 6:
            # Extract status code and file size
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size

                # Update the status code count if valid
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (ValueError, IndexError):
                continue
        
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    handle_exit(None, None)
