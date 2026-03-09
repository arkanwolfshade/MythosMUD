# MythosMUD Makefile

# Project root detection (handles worktree contexts)
PROJECT_ROOT := $(if $(findstring MythosMUD-,$(CURDIR)),$(abspath $(CURDIR)/..),$(CURDIR))

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
.PHONY: help clean install build run run-production apply-procedures
.PHONY: lint lint-sqlalchemy format mypy
.PHONY: bandit pylint ruff sqlfluff sqlint
.PHONY: hadolint shellcheck psscriptanalyzer
.PHONY: stylelint markdownlint jackson-linter
.PHONY: trivy lizard
.PHONY: codacy-tools
.PHONY: setup-test-env setup-test-env-force check-postgresql setup-postgresql-test-db verify-schema
.PHONY: test test-coverage test-client test-client-e2e test-playwright test-client-coverage test-server test-server-coverage test-ci
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
	@echo "  markdownlint   - Markdown linter (use ARGS='--fix' to auto-fix)"
	@echo "  jackson-linter - JSON linter"
	@echo "  trivy          - Dependency security scanner"
	@echo "  lizard         - Code complexity analyzer"
	@echo "  codacy-tools   - Run all Codacy tools"
	@echo ""
	@echo "Database Setup:"
	@echo "  setup-test-env         - Create test environment files"
	@echo "  setup-test-env-force  - Overwrite .env.unit_test from template (PostgreSQL)"
	@echo "  check-postgresql       - Verify PostgreSQL connectivity"
	@echo "  setup-postgresql-test-db - Create PostgreSQL test database"
	@echo "  verify-schema          - Verify db/mythos_<env>_ddl.sql matches database"
	@echo ""
	@echo "Documentation:"
	@echo "  openapi-spec          - Generate OpenAPI spec to docs/openapi/openapi.json"
	@echo ""
	@echo "Testing:"
	@echo "  test                  - Run all tests (client + server, no coverage)"
	@echo "  test-coverage         - Run all tests with coverage"
	@echo "  test-client           - Run client unit tests only (no coverage)"
	@echo "  test-client-e2e       - Run client E2E tests (Playwright)"
	@echo "  test-playwright   - Run client E2E + server integration tests (requires running server; mucks with runtime data)"
	@echo "  test-client-coverage  - Run client unit tests with coverage"
	@echo "  test-server           - Run server tests only (no coverage)"
	@echo "  test-server-coverage  - Run server tests with coverage"
	@echo "  test-ci               - CI/CD test suite (enforces coverage thresholds)"
	@echo ""
	@echo "Build & Deploy:"
	@echo "  clean             - Remove build, dist, and cache files"
	@echo "  install           - Install dependencies (worktree-aware)"
	@echo "  build             - Apply procedures, then build the client (Node)"
	@echo "  apply-procedures  - Apply db/procedures/*.sql to target databases"
	@echo "  run               - Start the development server (Uvicorn)"
	@echo "  run-production    - Start the server for production (Gunicorn + Uvicorn workers)"
	@echo ""
	@echo "Note: Server integration tests run under test-playwright (with running server). Unit only: make test-server."
	@echo "  uv run pytest -m unit server/tests   # unit only"
	@echo "  See TESTING.md for details."

# ============================================================================
# CODE QUALITY
# ============================================================================

# Ruff command in scripts/lint.py matches CI (.github/workflows/ci.yml "Lint with ruff")
# so local make lint fails on the same issues as CI
lint:
	$(PYTHON) scripts/lint.py
	$(PYTHON) scripts/check_logging_consistency.py
	$(PYTHON) scripts/check_asyncio_run_guardrails.py
	$(PYTHON) scripts/lint_sql_guardrails.py

lint-sqlalchemy:
	$(PYTHON) scripts/lint_sqlalchemy_async.py

# CRITICAL: CI/CD uses the same command (pre-commit run mypy --all-files)
# If you change this, update .github/workflows/ci.yml to match
mypy:
	$(UV) pre-commit run mypy --all-files

format:
	$(PYTHON) scripts/format.py

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

# Lightweight guardrails for hand-maintained SQL (select *, NOT IN subquery)
lint-sql-guardrails:
	$(PYTHON) scripts/lint_sql_guardrails.py

# Forbid asyncio.run() in server/ (AnyIO best practice; use anyio.run() at entry points)
lint-asyncio-run-guardrails:
	$(PYTHON) scripts/check_asyncio_run_guardrails.py

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
	$(PYTHON) scripts/markdownlint.py $(ARGS)

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

# Overwrite .env.unit_test from env.unit_test.example (use when file has stale SQLite URL)
setup-test-env-force:
	@echo "Refreshing test environment from template (overwrite)..."
	$(POWERSHELL) scripts/setup_test_environment.ps1 -Force

check-postgresql:
	@echo "Checking PostgreSQL connectivity..."
	$(POWERSHELL) scripts/check_postgresql.ps1

setup-postgresql-test-db:
	@echo "Setting up PostgreSQL test database..."
	$(POWERSHELL) scripts/setup_postgresql_test_db.ps1

verify-schema:
	@echo "Verifying environment DDL matches database (from .env.local or .env)..."
	$(POWERSHELL) scripts/verify_schema_match.ps1

# ============================================================================
# DOCUMENTATION
# ============================================================================

openapi-spec:
	@echo "Generating OpenAPI spec..."
	$(UV) python scripts/generate_openapi_spec.py

# ============================================================================
# TESTING
# ============================================================================

test-client:
	@echo "Running client unit tests (no coverage)..."
	cd $(PROJECT_ROOT)/client && npm run test:unit:run

test-client-e2e:
	@echo "Running client E2E tests (Playwright)..."
	cd $(PROJECT_ROOT)/client && npm run test

# Integration tests (server pytest -m integration) run here: they muck with runtime data
# and belong in the same flow as Playwright (running server context). They are NOT run by make test-server.
test-playwright: setup-test-env setup-postgresql-test-db
	$(POWERSHELL) scripts/apply_procedures.ps1 -TargetDbs mythos_e2e
	$(POWERSHELL) scripts/apply_coc_spells_migration.ps1 -TargetDbs mythos_e2e
	$(POWERSHELL) scripts/apply_arena_migration.ps1 -TargetDbs mythos_e2e
	@echo "Running client E2E runtime tests (Playwright CLI)..."
	cd $(PROJECT_ROOT)/client && npm run test:e2e:runtime
	@echo "Running server integration tests (runtime DB, single worker)..."
	$(UV) pytest server/tests/ -m integration -n 1 $(PYTEST_OPTS)

test-client-coverage:
	@echo "Running client unit tests with coverage..."
	cd $(PROJECT_ROOT)/client && npm run test:coverage

test-server: setup-test-env setup-postgresql-test-db
	@echo "Running server tests (no coverage)..."
	$(POWERSHELL) scripts/apply_procedures.ps1 -TargetDbs mythos_unit
	$(POWERSHELL) scripts/apply_coc_spells_migration.ps1 -TargetDbs mythos_unit
	$(POWERSHELL) scripts/apply_arena_migration.ps1 -TargetDbs mythos_unit
	$(UV) pytest server/tests/ -m "not integration" $(PYTEST_OPTS)

test-server-coverage: setup-test-env setup-postgresql-test-db
	@echo "Running server tests with coverage..."
	$(POWERSHELL) scripts/apply_procedures.ps1 -TargetDbs mythos_unit
	$(POWERSHELL) scripts/apply_coc_spells_migration.ps1 -TargetDbs mythos_unit
	$(POWERSHELL) scripts/apply_arena_migration.ps1 -TargetDbs mythos_unit
	$(UV) pytest server/tests/ -m "not integration" $(PYTEST_OPTS) $(PYTEST_COV_OPTS)

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

build: apply-procedures
	$(PYTHON) scripts/build.py

apply-procedures:
	@echo "Applying PostgreSQL procedures to mythos_dev..."
	$(POWERSHELL) scripts/apply_procedures.ps1 -TargetDbs mythos_dev

run:
	$(PYTHON) scripts/run.py

# Production: Gunicorn with Uvicorn workers (see docs/deployment.md)
# Default port 8000; for another port run the gunicorn command with -b 0.0.0.0:PORT
run-production:
	$(UV) gunicorn server.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000

# ============================================================================
# COMPOSITE TARGETS
# ============================================================================

all: format mypy lint lint-sqlalchemy codacy-tools check-postgresql build openapi-spec test-coverage
