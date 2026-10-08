"""Command line interface entrypoint for hello-python."""

import sys
from .core import (
    format_pascals_triangle,
    generate_pascals_triangle,
    get_greeting,
    get_today_date,
)


def main() -> int:
    """Execute main application workflow and print to stdout."""
    # 1. Self introduction
    print(get_greeting())

    # 2. Today's date
    today = get_today_date()
    print(f"Today's date: {today}")

    # 3. Pascal's triangle with rows equal to today's day (dd)
    rows = today.day
    print(f"\nPascal's Triangle ({rows} rows):")

    triangle = generate_pascals_triangle(rows)
    formatted_lines = format_pascals_triangle(triangle)
    for line in formatted_lines:
        print(line)

    return 0


if __name__ == "__main__":
    sys.exit(main())
