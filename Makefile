# MythosMUD Makefile

.PHONY: help clean lint format test test-ci test-coverage test-client test-client-coverage test-server test-server-coverage coverage build install run semgrep semgrep-autofix mypy lint-sqlalchemy setup-test-env check-postgresql setup-postgresql-test-db verify-schema

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
	@echo "Database Setup:"
	@echo "  setup-test-env         - Create test environment files"
	@echo "  check-postgresql       - Verify PostgreSQL connectivity for tests"
	@echo "  setup-postgresql-test-db - Create PostgreSQL test database"
	@echo "  verify-schema          - Verify authoritative_schema.sql matches mythos_dev"
	@echo ""
	@echo "Testing:"
	@echo "  test                  - Run all tests (client + server, no coverage)"
	@echo "  test-coverage         - Run all tests with coverage (client + server)"
	@echo "  test-client           - Run client tests only (no coverage)"
	@echo "  test-client-coverage  - Run client tests with coverage"
	@echo "  test-server           - Run server tests only (no coverage)"
	@echo "  test-server-coverage  - Run server tests with coverage"
	@echo "  test-ci               - CI/CD test suite (with coverage, enforces thresholds)"
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

check-postgresql:
	@echo "Checking PostgreSQL connectivity for tests..."
	cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File scripts/check_postgresql.ps1

setup-postgresql-test-db:
	@echo "Setting up PostgreSQL test database..."
	cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File scripts/setup_postgresql_test_db.ps1

verify-schema:
	@echo "Verifying authoritative_schema.sql matches mythos_dev..."
	cd $(PROJECT_ROOT) && powershell -ExecutionPolicy Bypass -File scripts/verify_schema_match.ps1

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
# TESTING TARGETS
# ============================================================================

# Client tests (no coverage)
test-client:
	@echo "Running client tests (unit + E2E, no coverage)..."
	cd $(PROJECT_ROOT)/client && npm run test:unit:run
	cd $(PROJECT_ROOT)/client && npm run test

# Client tests (with coverage)
test-client-coverage:
	@echo "Running client tests with coverage..."
	cd $(PROJECT_ROOT)/client && npm run test:coverage
	cd $(PROJECT_ROOT)/client && npm run test

# Server tests (no coverage)
test-server: setup-test-env
	@echo "Running server tests (no coverage)..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/ -n auto --maxfail=10 --tb=short

# Server tests (with coverage)
test-server-coverage: setup-test-env
	@echo "Running server tests with coverage..."
	cd $(PROJECT_ROOT) && uv run pytest server/tests/ --cov=server --cov-report=html --cov-report=term-missing --cov-report=xml -n auto --maxfail=10 --tb=short

# All tests (client + server, no coverage)
test: test-client test-server

# All tests (client + server, with coverage)
test-coverage: test-client-coverage test-server-coverage

# CI/CD test suite (with coverage, enforces thresholds)
# Runs in Docker locally to match CI/CD Ubuntu environment
# Runs directly when already in CI/CD environment (detected via CI or GITHUB_ACTIONS env vars)
ACT_RUNNER_IMAGE := mythosmud-gha-runner:latest
ACT_RUNNER_DOCKERFILE := Dockerfile.github-runner

test-ci:
	@if [ -n "$$CI" ] || [ -n "$$GITHUB_ACTIONS" ]; then \
		echo "Running CI test suite directly (already in CI environment)..."; \
		cd $(PROJECT_ROOT)/client && npm run test:coverage; \
		cd $(PROJECT_ROOT)/client && npm run test; \
		cd $(PROJECT_ROOT) && source .venv-ci/bin/activate && pytest server/tests/ --cov=server --cov-report=xml --cov-report=html --cov-fail-under=80 -v --tb=short; \
	else \
		echo "Building Docker runner image (this ensures dependencies are up-to-date)..."; \
		cd $(PROJECT_ROOT) && docker build --pull -t $(ACT_RUNNER_IMAGE) -f $(ACT_RUNNER_DOCKERFILE) .; \
		echo "Running CI test suite in Docker (coverage enforced)..."; \
		echo "Starting PostgreSQL service in container..."; \
		docker run --rm \
			-v "$(PROJECT_ROOT):/workspace" \
			-w /workspace \
			$(ACT_RUNNER_IMAGE) \
			bash -c "service postgresql start && sleep 3 && \
			cd /workspace/client && npm run test:coverage && \
			cd /workspace/client && npm run test && \
			cd /workspace && source .venv/bin/activate && \
			pytest server/tests/ --cov=server --cov-report=xml --cov-report=html --cov-fail-under=80 -v --tb=short"; \
	fi

# Legacy alias for backward compatibility
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
	cd $(PROJECT_ROOT) && make semgrep
	cd $(PROJECT_ROOT) && make build
	cd $(PROJECT_ROOT) && make test-coverage
