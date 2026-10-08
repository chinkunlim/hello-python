"""Hello Python package.

A modern modular Python package demonstrating evolution from a simple script
to an enterprise-grade project with conversation traceability.
"""

from .core import (
    format_pascals_triangle,
    generate_pascals_triangle,
    get_greeting,
    get_today_date,
)

__version__ = "4.0.0"
__all__ = [
    "get_greeting",
    "get_today_date",
    "generate_pascals_triangle",
    "format_pascals_triangle",
]
