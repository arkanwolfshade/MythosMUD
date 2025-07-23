# MythosMUD Makefile

.PHONY: help clean lint format test coverage build

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
	cd server && flake8
	cd client && npx eslint .

format:
	cd server && black .
	cd client && npx prettier --write .

test:
	cd server && pytest
	# Add client tests here if/when available

coverage:
	cd server && pytest --cov=world_loader --cov-report=term-missing

build:
	cd client && npm run build 