"""Backward-compatible root entrypoint for hello-python.

Delegates execution to the modular src-layout package `src/hello_python/cli.py`.
"""

import sys
from pathlib import Path

# Ensure src directory is on sys.path for direct execution
SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from hello_python.cli import main

if __name__ == "__main__":
    sys.exit(main())
