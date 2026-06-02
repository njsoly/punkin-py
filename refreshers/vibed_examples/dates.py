#!/usr/bin/env python3

import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
import os

DEBUG = True

YEAR_4 = r'[12]\d{3}'
DAY_2 = r'(0[1-9]|[12]\d|3[01])'
MONTH_2 = r'(0[1-9]|1[0-2])'

DATE_FORMATS = {
    'yyyy_mm_dd': {
        'regex': re.compile('^' + YEAR_4 + '[-_]?' + MONTH_2 + '[-_]?' + DAY_2 + '$'),
        'description': 'YYYY-MM-DD',
        'parser': lambda s: datetime.strptime(re.sub(r'[-_]', '', s), '%Y%m%d')
    },
    'yyyy_mm_dd_hh_mm_ss': {
        'regex': re.compile('^' + YEAR_4 + '-' + MONTH_2 + '-' + DAY_2 + r' ([01]\d|2[0-3]):[0-5]\d:[0-5]\d$'),
        'description': 'YYYY-MM-DD HH:MM:SS',
        'parser': lambda s: datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    },
    'yymmdd': {
        'regex': re.compile(r'^\d{2}' + MONTH_2 + DAY_2 + '$'),
        'description': 'YYMMDD',
        'parser': lambda s: datetime.strptime(s, '%y%m%d')
    },
    'yyyy': {
        'regex': re.compile('^' + YEAR_4 + '$'),
        'description': 'YYYY',
        'parser': lambda s: datetime.strptime(s, '%Y')
    },
    'unix_epoch': {
        'regex': re.compile(r'^\d+$'),
        'description': 'Unix Epoch (seconds since 1970)',
        'parser': lambda s: datetime.fromtimestamp(int(s))
    },
    'm_d_yyyy': {
        'regex': re.compile(r'^\d{1,2}/\d{1,2}/' + YEAR_4 + '$'),
        'description': 'M/D/YYYY',
        'parser': lambda s: datetime.strptime(s, '%m/%d/%Y')
    }
}


def get_timezone():
    """Get the user's timezone, falling back to system timezone, then UTC."""
    try:
        tz_name = os.environ.get('TZ')
        if tz_name:
            return ZoneInfo(tz_name)
    except Exception:
        pass

    try:
        localtime_path = '/etc/localtime'
        if os.path.exists(localtime_path):
            real_path = os.path.realpath(localtime_path)
            if '/zoneinfo/' in real_path:
                tz_name = real_path.split('/zoneinfo/')[-1]
                return ZoneInfo(tz_name)
    except Exception:
        pass

    return ZoneInfo('UTC')


def identify_format(date_string):
    """Identify the format of a date string using regex patterns."""
    for format_name, format_info in DATE_FORMATS.items():
        if format_info['regex'].match(date_string):
            return format_name, format_info
    return None, None


def convert_to_human_readable(date_string):
    """Convert a date string to YYYY-MM-DD HH:MM:SS in local timezone."""
    format_name, format_info = identify_format(date_string)

    if not format_info:
        return f"Error: Unable to identify format for '{date_string}'"

    if DEBUG:
        print(f"[DEBUG] Detected format: {format_info['description']}")

    try:
        dt = format_info['parser'](date_string)

        tz = get_timezone()

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=tz)

        local_dt = dt.astimezone(tz)

        result = local_dt.strftime('%Y-%m-%d %H:%M:%S')
        tz_name = str(tz)

        return f"{result} ({tz_name})"

    except Exception as e:
        return f"Error parsing date: {e}"


def print_menu():
    """Display the interactive menu."""
    print("\n=== Date Conversion Menu ===")
    print("1. Convert a date/time")
    print("2. Quit")
    print("============================")


def interactive_mode():
    """Run the interactive mode."""
    print("Welcome to the Date Converter!")
    print("This tool converts various date formats to human-readable local time.")

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-2): ").strip()

        if choice == '1':
            date_input = input("Enter date/time to convert: ").strip()
            if date_input:
                result = convert_to_human_readable(date_input)
                print(f"\nResult: {result}")
            else:
                print("No input provided.")

        elif choice == '2':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


def main():
    """Main entry point for the script."""
    if len(sys.argv) == 2:
        date_string = sys.argv[1]
        result = convert_to_human_readable(date_string)
        print(result)

    elif len(sys.argv) == 1:
        interactive_mode()

    else:
        print("Usage: dates.py [date_string]")
        print("  With one argument: converts the date to YYYY-MM-DD HH:MM:SS")
        print("  With no arguments: enters interactive mode")
        sys.exit(1)


if __name__ == '__main__':
    main()
