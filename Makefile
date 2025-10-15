# MythosMUD Makefile

.PHONY: help clean lint format test coverage build install run semgrep test-client-e2e test-server-e2e lint-sqlalchemy test-unit test-integration test-e2e test-security test-performance test-coverage test-regression test-monitoring test-verification test-all test-fast test-slow

# Determine project root for worktree contexts
PROJECT_ROOT := $(shell python -c "import os; print(os.path.dirname(os.getcwd()) if 'MythosMUD-' in os.getcwd() else os.getcwd())")

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build, dist, and cache files"
	@echo "  lint      - Run ruff (Python) and ESLint (Node)"
	@echo "  lint-sqlalchemy - Run SQLAlchemy async pattern linter"
	@echo "  format    - Run ruff format (Python) and Prettier (Node)"
	@echo "  test      - Run all tests (server + client)"
	@echo "  test-server - Run server tests only"
	@echo "  test-client - Run client unit tests only (Vitest)"
	@echo "  test-client-e2e - Run automated client E2E tests (Playwright e2e)"
	@echo "  test-server-e2e - Run server E2E tests (requires running server)"
	@echo "  coverage  - Run coverage for both server and client"
	@echo "  build     - Build the client (Node)"
	@echo "  install   - Install dependencies (worktree-aware)"
	@echo "  semgrep   - Run Semgrep static analysis (security and best practices)"
	@echo ""
	@echo "E2E Testing:"
	@echo "  make test-client-e2e  - Automated single-player E2E tests (fast)"
	@echo "  See e2e-tests/MULTIPLAYER_TEST_RULES.md for multi-player MCP scenarios"

clean:
	cd $(PROJECT_ROOT) && python scripts/clean.py

lint:
	cd $(PROJECT_ROOT) && python scripts/lint.py
	cd $(PROJECT_ROOT) && python scripts/check_logging_consistency.py

lint-sqlalchemy:
	cd $(PROJECT_ROOT) && python scripts/lint_sqlalchemy_async.py

format:
	cd $(PROJECT_ROOT) && python scripts/format.py

test:
	cd $(PROJECT_ROOT) && python scripts/test.py

test-server:
	cd $(PROJECT_ROOT) && python scripts/test.py --server-only

test-client:
	cd $(PROJECT_ROOT) && python scripts/test.py --client-only

test-client-e2e:
	cd $(PROJECT_ROOT) && python scripts/test.py --client-e2e-only

test-server-e2e:
	cd $(PROJECT_ROOT) && python scripts/test.py --server-e2e-only

# New hierarchical test targets
test-unit:
	cd $(PROJECT_ROOT) && pytest server/tests/unit -v

test-integration:
	cd $(PROJECT_ROOT) && pytest server/tests/integration -v

test-e2e:
	cd $(PROJECT_ROOT) && pytest server/tests/e2e -v

test-security:
	cd $(PROJECT_ROOT) && pytest server/tests/security -v

test-performance:
	cd $(PROJECT_ROOT) && pytest server/tests/performance -v

test-coverage:
	cd $(PROJECT_ROOT) && pytest server/tests/coverage -v

test-regression:
	cd $(PROJECT_ROOT) && pytest server/tests/regression -v

test-monitoring:
	cd $(PROJECT_ROOT) && pytest server/tests/monitoring -v

test-verification:
	cd $(PROJECT_ROOT) && pytest server/tests/verification -v

test-all:
	cd $(PROJECT_ROOT) && pytest server/tests -v

test-fast:
	cd $(PROJECT_ROOT) && pytest server/tests/unit -v -x

test-slow:
	cd $(PROJECT_ROOT) && pytest server/tests -v -m slow

coverage:
	cd $(PROJECT_ROOT) && python scripts/coverage.py

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
	cd $(PROJECT_ROOT) && make lint
	cd $(PROJECT_ROOT) && make coverage
	cd $(PROJECT_ROOT) && make build
