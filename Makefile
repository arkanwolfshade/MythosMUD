# MythosMUD Makefile

.PHONY: help clean lint format test coverage build install run

# Determine project root for worktree contexts
PROJECT_ROOT := $(shell python -c "import os; print(os.path.dirname(os.getcwd()) if 'MythosMUD-' in os.getcwd() else os.getcwd())")

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build, dist, and cache files"
	@echo "  lint      - Run ruff (Python) and ESLint (Node)"
	@echo "  format    - Run ruff format (Python) and Prettier (Node)"
	@echo "  test      - Run Python and Node tests (includes test DB cleanup)"
	@echo "  coverage  - Run Python tests with coverage"
	@echo "  build     - Build the client (Node)"
	@echo "  install   - Install dependencies (worktree-aware)"

clean:
	cd $(PROJECT_ROOT) && python scripts/clean.py

lint:
	cd $(PROJECT_ROOT) && python scripts/lint.py

format:
	cd $(PROJECT_ROOT) && python scripts/format.py

test:
	cd $(PROJECT_ROOT) && python scripts/test.py

coverage:
	cd $(PROJECT_ROOT) && python scripts/coverage.py

build:
	cd $(PROJECT_ROOT) && python scripts/build.py

install:
	cd $(PROJECT_ROOT) && python scripts/install.py

run:
	cd $(PROJECT_ROOT) && python scripts/run.py

all:
	cd $(PROJECT_ROOT) && make format
	cd $(PROJECT_ROOT) && make lint
	cd $(PROJECT_ROOT) && make test
