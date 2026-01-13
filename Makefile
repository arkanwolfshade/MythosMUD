# MythosMUD Makefile

# Project root detection (handles worktree contexts)
PROJECT_ROOT := $(shell python -c "import os; print(os.path.dirname(os.getcwd()) if 'MythosMUD-' in os.getcwd() else os.getcwd())")

# Common command patterns
PYTHON := cd $(PROJECT_ROOT) && python
UV := cd $(PROJECT_ROOT) && uv run
POWERSHELL := cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File

# Pytest common options
# Note: -n auto is already in pytest.ini addopts, so we don't duplicate it here
PYTEST_OPTS := --maxfail=10 --tb=short
# Coverage options: pytest-cov automatically aggregates worker coverage when used with pytest-xdist
# The --cov option must be specified, and pytest-cov will handle worker aggregation
PYTEST_COV_OPTS := --cov=server --cov-report=html --cov-report=term-missing --cov-report=xml

# PHONY targets
.PHONY: help clean install build run
.PHONY: lint lint-sqlalchemy format mypy
.PHONY: semgrep semgrep-autofix
.PHONY: bandit pylint ruff sqlfluff sqlint
.PHONY: hadolint shellcheck psscriptanalyzer
.PHONY: stylelint markdownlint jackson-linter
.PHONY: trivy lizard
.PHONY: codacy-tools
.PHONY: setup-test-env check-postgresql setup-postgresql-test-db verify-schema
.PHONY: test test-coverage test-client test-client-coverage test-server test-server-coverage test-ci
.PHONY: coverage all

# ============================================================================
# HELP
# ============================================================================

help:
	@echo "MythosMUD Development Commands"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint            - Run ruff (Python) and ESLint (Node)"
	@echo "  lint-sqlalchemy - Run SQLAlchemy async pattern linter"
	@echo "  format          - Run ruff format (Python) and Prettier (Node)"
	@echo "  mypy            - Run mypy static type checking"
	@echo "  semgrep         - Run Semgrep security analysis"
	@echo "  semgrep-autofix - Run Semgrep with autofix"
	@echo ""
	@echo "Codacy Tools (Python):"
	@echo "  bandit          - Python security linter"
	@echo "  pylint         - Python code quality linter"
	@echo "  sqlfluff       - SQL linting and formatting"
	@echo "  sqlint         - SQL linting"
	@echo ""
	@echo "Codacy Tools (Other):"
	@echo "  hadolint       - Dockerfile linter"
	@echo "  shellcheck     - Shell script linter"
	@echo "  psscriptanalyzer - PowerShell script linter"
	@echo "  stylelint      - CSS linter"
	@echo "  markdownlint   - Markdown linter"
	@echo "  jackson-linter - JSON linter"
	@echo "  trivy          - Dependency security scanner"
	@echo "  lizard         - Code complexity analyzer"
	@echo "  codacy-tools   - Run all Codacy tools"
	@echo ""
	@echo "Database Setup:"
	@echo "  setup-test-env         - Create test environment files"
	@echo "  check-postgresql       - Verify PostgreSQL connectivity"
	@echo "  setup-postgresql-test-db - Create PostgreSQL test database"
	@echo "  verify-schema          - Verify authoritative_schema.sql matches mythos_dev"
	@echo ""
	@echo "Testing:"
	@echo "  test                  - Run all tests (client + server, no coverage)"
	@echo "  test-coverage         - Run all tests with coverage"
	@echo "  test-client           - Run client tests only (no coverage)"
	@echo "  test-client-coverage - Run client tests with coverage"
	@echo "  test-server           - Run server tests only (no coverage)"
	@echo "  test-server-coverage  - Run server tests with coverage"
	@echo "  test-ci               - CI/CD test suite (enforces coverage thresholds)"
	@echo ""
	@echo "Build & Deploy:"
	@echo "  clean           - Remove build, dist, and cache files"
	@echo "  install         - Install dependencies (worktree-aware)"
	@echo "  build           - Build the client (Node)"
	@echo "  run             - Start the development server"
	@echo ""
	@echo "Note: For tiered server testing (unit/integration/e2e), use pytest markers directly:"
	@echo "  uv run pytest -m unit server/tests"
	@echo "  See TESTING.md for details."

# ============================================================================
# CODE QUALITY
# ============================================================================

lint:
	$(PYTHON) scripts/lint.py
	$(PYTHON) scripts/check_logging_consistency.py

lint-sqlalchemy:
	$(PYTHON) scripts/lint_sqlalchemy_async.py

# CRITICAL: CI/CD uses the same command (pre-commit run mypy --all-files)
# If you change this, update .github/workflows/ci.yml to match
mypy:
	$(UV) pre-commit run mypy --all-files

format:
	$(PYTHON) scripts/format.py

semgrep:
	$(PYTHON) scripts/semgrep.py

semgrep-autofix:
	$(POWERSHELL) scripts/semgrep-autofix.ps1

# ============================================================================
# CODACY TOOLS - Python
# ============================================================================

bandit:
	$(PYTHON) scripts/bandit.py

pylint:
	$(PYTHON) scripts/pylint.py

sqlfluff:
	$(PYTHON) scripts/sqlfluff.py

sqlint:
	$(PYTHON) scripts/sqlint.py

# ============================================================================
# CODACY TOOLS - Other Languages
# ============================================================================

hadolint:
	$(POWERSHELL) scripts/hadolint.ps1

shellcheck:
	$(POWERSHELL) scripts/shellcheck.ps1

psscriptanalyzer:
	$(POWERSHELL) scripts/psscriptanalyzer.ps1

stylelint:
	$(PYTHON) scripts/stylelint.py

markdownlint:
	$(PYTHON) scripts/markdownlint.py

jackson-linter:
	$(PYTHON) scripts/jackson_linter.py

trivy:
	$(PYTHON) scripts/trivy.py

lizard:
	$(PYTHON) scripts/lizard.py

# Run all Codacy tools (except those already in lint/format)
codacy-tools: bandit pylint sqlfluff hadolint shellcheck psscriptanalyzer stylelint markdownlint jackson-linter trivy lizard

# ============================================================================
# DATABASE SETUP
# ============================================================================

setup-test-env:
	@echo "Setting up test environment files..."
	$(POWERSHELL) scripts/setup_test_environment.ps1

check-postgresql:
	@echo "Checking PostgreSQL connectivity..."
	$(POWERSHELL) scripts/check_postgresql.ps1

setup-postgresql-test-db:
	@echo "Setting up PostgreSQL test database..."
	$(POWERSHELL) scripts/setup_postgresql_test_db.ps1

verify-schema:
	@echo "Verifying authoritative_schema.sql matches mythos_dev..."
	$(POWERSHELL) scripts/verify_schema_match.ps1

# ============================================================================
# TESTING
# ============================================================================

test-client:
	@echo "Running client tests (unit + E2E, no coverage)..."
	cd $(PROJECT_ROOT)/client && npm run test:unit:run
	cd $(PROJECT_ROOT)/client && npm run test

test-client-coverage:
	@echo "Running client tests with coverage..."
	cd $(PROJECT_ROOT)/client && npm run test:coverage
	cd $(PROJECT_ROOT)/client && npm run test

test-server: setup-test-env
	@echo "Running server tests (no coverage)..."
	$(UV) pytest server/tests/ $(PYTEST_OPTS)

test-server-coverage: setup-test-env
	@echo "Running server tests with coverage..."
	$(UV) pytest server/tests/ $(PYTEST_OPTS) $(PYTEST_COV_OPTS)

test: test-client test-server

test-coverage: test-client-coverage test-server-coverage

# CI/CD test suite (with coverage, enforces thresholds)
# Runs in Docker locally to match CI/CD Ubuntu environment
# Runs directly when already in CI/CD environment (detected via CI or GITHUB_ACTIONS env vars)
# CI/CD test suite (with coverage, enforces thresholds)
# run_test_ci.py automatically detects and uses .venv-ci or .venv if available
# This ensures local test-ci matches CI environment behavior
test-ci:
	$(PYTHON) scripts/run_test_ci.py

# Legacy alias for backward compatibility
coverage: test-coverage

# ============================================================================
# BUILD & DEPLOY
# ============================================================================

clean:
	$(PYTHON) scripts/clean.py

install:
	$(PYTHON) scripts/install.py

build:
	$(PYTHON) scripts/build.py

run:
	$(PYTHON) scripts/run.py

# ============================================================================
# COMPOSITE TARGETS
# ============================================================================

all: format mypy lint lint-sqlalchemy codacy-tools semgrep-autofix codacy-tools build test-coverage
