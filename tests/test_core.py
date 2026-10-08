"""Unit tests for hello_python.core module."""

import datetime
import unittest

from hello_python.core import (
    format_pascals_triangle,
    generate_pascals_triangle,
    get_greeting,
    get_today_date,
)


class TestCoreFunctions(unittest.TestCase):
    """Test cases for core greeting, date, and Pascal's triangle functions."""

    def test_greeting_default(self) -> None:
        """Test default greeting uses GitHub username chinkunlim and protects privacy."""
        greeting = get_greeting()
        self.assertIn("chinkunlim", greeting)
        self.assertEqual(greeting, "Hello, I am chinkunlim! Welcome to my Python project.")

    def test_greeting_custom(self) -> None:
        """Test custom username parameter in greeting."""
        greeting = get_greeting("octocat")
        self.assertEqual(greeting, "Hello, I am octocat! Welcome to my Python project.")

    def test_today_date(self) -> None:
        """Test get_today_date returns valid date object."""
        today = get_today_date()
        self.assertIsInstance(today, datetime.date)
        self.assertEqual(today, datetime.date.today())

    def test_pascals_triangle_empty(self) -> None:
        """Test edge cases with zero or negative row counts."""
        self.assertEqual(generate_pascals_triangle(0), [])
        self.assertEqual(generate_pascals_triangle(-5), [])

    def test_pascals_triangle_one_row(self) -> None:
        """Test single row Pascal's triangle."""
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_pascals_triangle_four_rows(self) -> None:
        """Test 4 rows calculation matching v3 state."""
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
        ]
        self.assertEqual(generate_pascals_triangle(4), expected)

    def test_format_pascals_triangle(self) -> None:
        """Test string formatting of triangle lines."""
        triangle = generate_pascals_triangle(4)
        formatted = format_pascals_triangle(triangle, width_factor=4)
        self.assertEqual(len(formatted), 4)
        # Verify each line has content
        for line in formatted:
            self.assertTrue(line.strip().startswith("1"))


if __name__ == "__main__":
    unittest.main()
