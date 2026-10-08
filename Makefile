.PHONY: help sync test dev lint run check clean audit

# Test if uv is executable in current environment
UV_EXEC := $(shell uv --version 2> /dev/null)

help:
	@echo "Available commands:"
	@echo "  make sync   - Synchronize dependencies (uv sync or pip check)"
	@echo "  make test   - Run unit tests (uv run pytest or python3 unittest)"
	@echo "  make dev    - Run application in development mode"
	@echo "  make lint   - Run linter (uv run ruff or syntax check)"
	@echo "  make run    - Run main entrypoint"
	@echo "  make audit  - Run Antigravity project compliance audit"
	@echo "  make clean  - Clean cache and build artifacts"

sync:
ifneq ($(UV_EXEC),)
	uv sync
else
	@echo "[Notice] uv not executable in current shell, using native python3 environment."
	python3 -m pip --version > /dev/null 2>&1 || true
endif

test:
ifneq ($(UV_EXEC),)
	uv run pytest tests/
else
	PYTHONPATH=src python3 -m unittest discover tests
endif

dev:
ifneq ($(UV_EXEC),)
	uv run python -m hello_python.cli
else
	PYTHONPATH=src python3 -m hello_python.cli
endif

lint:
ifneq ($(UV_EXEC),)
	uv run ruff check .
else
	python3 -m py_compile hello.py src/hello_python/*.py tests/*.py
	@echo "All files passed syntax check!"
endif

run:
	python3 hello.py

check: lint test

audit:
	python3 audit_project.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info
