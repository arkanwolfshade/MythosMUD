# MythosMUD Makefile

.PHONY: help clean lint format test coverage build install run

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build, dist, and cache files"
	@echo "  lint      - Run flake8 (Python) and ESLint (Node)"
	@echo "  format    - Run black (Python) and Prettier (Node)"
	@echo "  test      - Run Python and Node tests"
	@echo "  coverage  - Run Python tests with coverage"
	@echo "  build     - Build the client (Node)"

clean:
	rm -rf server/__pycache__ server/.pytest_cache server/htmlcov
	rm -rf client/dist client/node_modules

lint:
	cd server && ruff check .
	cd client && npx eslint .

format:
	cd server && ruff format .
	cd client && npx prettier --write .

test:
	PYTHONPATH=server pytest server/tests
	# Add client tests here if/when available

coverage:
	PYTHONPATH=server pytest --cov=world_loader --cov-report=term-missing server/tests

build:
	cd client && npm run build

install:
	python -m venv server/venv
	server/venv/Scripts/pip install --upgrade pip
	server/venv/Scripts/pip install -r server/requirements.txt
	cd client && nvm install && nvm use && npm install
	pip install pre-commit
	pre-commit install

run:
	cd server && venv/Scripts/python main.py
