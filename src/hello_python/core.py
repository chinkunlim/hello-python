"""Core business logic and algorithmic functions for hello-python."""

import datetime
from typing import List


def get_greeting(username: str = "chinkunlim") -> str:
    """Return a friendly self-introduction greeting protecting real identity."""
    return f"Hello, I am {username}! Welcome to my Python project."


def get_today_date() -> datetime.date:
    """Return today's date from system clock."""
    return datetime.date.today()


def generate_pascals_triangle(num_rows: int) -> List[List[int]]:
    """Generate Pascal's triangle with the specified number of rows.

    Args:
        num_rows: Number of rows to generate. Must be >= 0.

    Returns:
        A list of rows, where each row is a list of integers.
    """
    if num_rows <= 0:
        return []

    triangle: List[List[int]] = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def format_pascals_triangle(triangle: List[List[int]], width_factor: int = 4) -> List[str]:
    """Format Pascal's triangle rows as centered strings for terminal display.

    Args:
        triangle: Nested list representing Pascal's triangle.
        width_factor: Multiplier for total centered width.

    Returns:
        List of formatted string lines.
    """
    if not triangle:
        return []

    total_rows = len(triangle)
    total_width = total_rows * width_factor
    formatted_lines = []
    for row in triangle:
        line_str = " ".join(str(num) for num in row)
        formatted_lines.append(line_str.center(total_width))
    return formatted_lines
