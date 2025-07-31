# MythosMUD Makefile

.PHONY: help clean lint format test coverage build install run

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build, dist, and cache files"
	@echo "  lint      - Run ruff (Python) and ESLint (Node)"
	@echo "  format    - Run ruff format (Python) and Prettier (Node)"
	@echo "  test      - Run Python and Node tests (includes test DB cleanup)"
	@echo "  coverage  - Run Python tests with coverage"
	@echo "  build     - Build the client (Node)"

clean:
	python scripts/clean.py

lint:
	python scripts/lint.py

format:
	python scripts/format.py

test:
	python scripts/test.py

coverage:
	python scripts/coverage.py

build:
	python scripts/build.py

install:
	python scripts/install.py

run:
	python scripts/run.py
