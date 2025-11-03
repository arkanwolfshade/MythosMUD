# MythosMUD Makefile

.PHONY: help clean lint format test coverage build install run semgrep mypy test-client-e2e test-server-e2e lint-sqlalchemy test-unit test-integration test-e2e test-security test-performance test-coverage test-regression test-monitoring test-verification test-all test-fast test-slow setup-test-env

# Determine project root for worktree contexts
PROJECT_ROOT := $(shell python -c "import os; print(os.path.dirname(os.getcwd()) if 'MythosMUD-' in os.getcwd() else os.getcwd())")

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build, dist, and cache files"
	@echo "  lint      - Run ruff (Python) and ESLint (Node)"
	@echo "  lint-sqlalchemy - Run SQLAlchemy async pattern linter"
	@echo "  mypy      - Run mypy static type checking"
	@echo "  format    - Run ruff format (Python) and Prettier (Node)"
	@echo "  test      - Run all tests (server + client)"
	@echo "  test-server - Run server tests only (unit + integration)"
	@echo "  test-client - Run client unit tests only (Vitest)"
	@echo "  test-client-e2e - Run automated client E2E tests (Playwright e2e)"
	@echo "  test-server-e2e - Run server E2E tests (requires running server)"
	@echo "  test-unit - Run unit tests only"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-e2e - Run E2E tests only"
	@echo "  test-security - Run security tests only"
	@echo "  test-performance - Run performance tests only"
	@echo "  test-coverage - Generate coverage report only"
	@echo "  test-regression - Run regression tests only"
	@echo "  test-monitoring - Run monitoring tests only"
	@echo "  test-verification - Run verification tests only"
	@echo "  test-all - Run all tests (unit + integration, excluding E2E)"
	@echo "  test-fast - Run unit tests with fail-fast mode"
	@echo "  test-slow - Run slow tests only"
	@echo "  coverage  - Run coverage for both server and client"
	@echo "  build     - Build the client (Node)"
	@echo "  install   - Install dependencies (worktree-aware)"
	@echo "  semgrep   - Run Semgrep static analysis (security and best practices)"
	@echo "  setup-test-env - Setup test environment files (required before running tests)"
	@echo ""
	@echo "E2E Testing:"
	@echo "  make test-client-e2e  - Automated single-player E2E tests (fast)"
	@echo "  See e2e-tests/MULTIPLAYER_TEST_RULES.md for multi-player MCP scenarios"

clean:
	cd $(PROJECT_ROOT) && python scripts/clean.py

setup-test-env:
	@echo "Setting up test environment files..."
	cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File scripts/setup_test_environment.ps1

lint:
	cd $(PROJECT_ROOT) && python scripts/lint.py
	cd $(PROJECT_ROOT) && python scripts/check_logging_consistency.py

lint-sqlalchemy:
	cd $(PROJECT_ROOT) && python scripts/lint_sqlalchemy_async.py

# CRITICAL: CI/CD uses the same command (pre-commit run mypy --all-files)
# If you change this, update .github/workflows/ci.yml to match
mypy:
	cd $(PROJECT_ROOT) && uv run pre-commit run mypy --all-files

format:
	cd $(PROJECT_ROOT) && python scripts/format.py

test: setup-test-env
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py

test-server: setup-test-env
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py

test-client:
	cd $(PROJECT_ROOT)/client && npm run test:unit:run

test-client-e2e:
	cd $(PROJECT_ROOT)/client && npm run test

test-server-e2e:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --e2e

# New hierarchical test targets
test-unit:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --unit

test-integration:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --integration

test-e2e:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --e2e

test-security:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --path server/tests/security

test-performance:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --path server/tests/performance

test-coverage:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --coverage

test-regression:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --path server/tests/regression

test-monitoring:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --path server/tests/monitoring

test-verification:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --path server/tests/verification

test-all:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py

test-fast:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --unit --pytest-args -x

test-slow:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --markers "slow"

coverage:
	cd $(PROJECT_ROOT) && uv run python scripts/test_runner.py --coverage

build:
	cd $(PROJECT_ROOT) && python scripts/build.py

install:
	cd $(PROJECT_ROOT) && python scripts/install.py

semgrep:
	cd $(PROJECT_ROOT) && python scripts/semgrep.py

run:
	cd $(PROJECT_ROOT) && python scripts/run.py

all:
	cd $(PROJECT_ROOT) && make format
	cd $(PROJECT_ROOT) && make mypy
	cd $(PROJECT_ROOT) && make lint
	cd $(PROJECT_ROOT) && make test-all
	cd $(PROJECT_ROOT) && make build
