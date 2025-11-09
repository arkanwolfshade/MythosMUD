# MythosMUD Makefile

.PHONY: help clean lint format test test-fast test-fast-serial test-comprehensive test-coverage test-client test-client-e2e test-e2e test-slow coverage build install run semgrep semgrep-autofix mypy lint-sqlalchemy setup-test-env

# Determine project root for worktree contexts
PROJECT_ROOT := $(shell python -c "import os; print(os.path.dirname(os.getcwd()) if 'MythosMUD-' in os.getcwd() else os.getcwd())")

help:
	@echo "Available targets:"
	@echo ""
	@echo "Code Quality:"
	@echo "  clean           - Remove build, dist, and cache files"
	@echo "  lint            - Run ruff (Python) and ESLint (Node)"
	@echo "  lint-sqlalchemy - Run SQLAlchemy async pattern linter"
	@echo "  mypy            - Run mypy static type checking"
	@echo "  format          - Run ruff format (Python) and Prettier (Node)"
	@echo ""
	@echo "Testing - Daily Development:"
	@echo "  test-fast        - Quick unit tests with parallelization (~2-3 min)"
	@echo "  test-fast-serial - Quick unit tests serially (for debugging)"
	@echo "  test             - Default pre-commit validation (~5-7 min target)"
	@echo "  test-client      - Client unit tests only (Vitest)"
	@echo "  test-client-e2e  - Automated client E2E tests (Playwright)"
	@echo ""
	@echo "Testing - CI/CD:"
	@echo "  test-comprehensive - Full test suite for CI/CD (~30 min)"
	@echo "  test-coverage      - Generate coverage reports"
	@echo ""
	@echo "Testing - On-Demand:"
	@echo "  test-e2e        - Server E2E tests (requires running services)"
	@echo "  test-slow       - All slow tests (performance, integration, etc.)"
	@echo ""
	@echo "Build & Deploy:"
	@echo "  build           - Build the client (Node)"
	@echo "  install         - Install dependencies (worktree-aware)"
	@echo "  semgrep         - Run Semgrep security analysis"
	@echo "  semgrep-autofix - Run Semgrep with autofix"
	@echo ""
	@echo "Note: See e2e-tests/MULTIPLAYER_TEST_RULES.md for multi-player MCP scenarios"

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

# ============================================================================
# TESTING TARGETS - Simplified Hierarchy
# ============================================================================

# ----------------------------------------------------------------------------
# Daily Development Workflow
# ----------------------------------------------------------------------------

test: setup-test-env
	@echo "Running default test suite (pre-commit validation, ~5-7 min target)..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/ -m "not slow and not e2e" -n auto --maxfail=10 --tb=short

test-client:
	@echo "Running client unit tests..."
	cd $(PROJECT_ROOT)/client && npm run test:unit:run

test-client-e2e:
	@echo "Running automated client E2E tests..."
	cd $(PROJECT_ROOT)/client && npm run test

# ----------------------------------------------------------------------------
# CI/CD Workflow
# ----------------------------------------------------------------------------

ACT_RUNNER_IMAGE := mythosmud-gha-runner:latest
ACT_RUNNER_DOCKERFILE := Dockerfile.github-runner

test-comprehensive: setup-test-env
	@echo "Running COMPREHENSIVE test suite via act (mirrors CI workflows)..."
	@if not exist "$(PROJECT_ROOT)\\.act.secrets" ( \
		echo ERROR: Missing $(PROJECT_ROOT)\\.act.secrets. Copy .act.secrets.example and populate secrets before running act. & \
		exit 1 )
	cd $(PROJECT_ROOT) && docker build -t $(ACT_RUNNER_IMAGE) -f $(ACT_RUNNER_DOCKERFILE) .
	cd $(PROJECT_ROOT) && act --env UV_PROJECT_ENVIRONMENT=.venv-ci --env UV_LINK_MODE=copy -W .github/workflows/ci.yml -j backend
	cd $(PROJECT_ROOT) && act --reuse --env UV_PROJECT_ENVIRONMENT=.venv-ci --env UV_LINK_MODE=copy -W .github/workflows/ci.yml -j frontend

test-coverage: setup-test-env
	@echo "Generating coverage report..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/ -m "not slow and not e2e" --cov --cov-report=html --cov-report=term-missing --cov-report=xml

# ----------------------------------------------------------------------------
# On-Demand Specialized Testing
# ----------------------------------------------------------------------------

test-e2e: setup-test-env
	@echo "Running server E2E tests (requires running services)..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/e2e/ -m "e2e" -v

test-slow: setup-test-env
	@echo "Running slow tests (performance, integration, etc.)..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/ -m "slow" -v

# ----------------------------------------------------------------------------
# Legacy Aliases (for backward compatibility)
# ----------------------------------------------------------------------------

coverage: test-coverage

build:
	cd $(PROJECT_ROOT) && python scripts/build.py

install:
	cd $(PROJECT_ROOT) && python scripts/install.py

semgrep:
	cd $(PROJECT_ROOT) && python scripts/semgrep.py

semgrep-autofix:
	cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File scripts/semgrep-autofix.ps1

run:
	cd $(PROJECT_ROOT) && python scripts/run.py

all:
	cd $(PROJECT_ROOT) && make format
	cd $(PROJECT_ROOT) && make mypy
	cd $(PROJECT_ROOT) && make lint
	cd $(PROJECT_ROOT) && make test-comprehensive
	cd $(PROJECT_ROOT) && make build
	cd $(PROJECT_ROOT) && make semgrep
