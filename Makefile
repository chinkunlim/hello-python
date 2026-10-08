.PHONY: help run test check clean

help:
	@echo "Available commands:"
	@echo "  make run    - Run the application"
	@echo "  make test   - Run all unit tests"
	@echo "  make check  - Run code syntax and import verification"
	@echo "  make clean  - Remove bytecode and cache directories"

run:
	python3 hello.py

test:
	PYTHONPATH=src python3 -m unittest discover tests

check:
	python3 -m py_compile hello.py src/hello_python/*.py tests/*.py
	@echo "All files passed syntax check!"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info
