# TestRunner

> 25 nodes

## Key Concepts

- **TestRunner** (13 connections) — `scripts/test_runner.py`
- **.run_tests()** (11 connections) — `scripts/test_runner.py`
- **test_runner.py** (7 connections) — `scripts/test_runner.py`
- **main()** (3 connections) — `scripts/test_runner.py`
- **.clean_test_databases()** (3 connections) — `scripts/test_runner.py`
- **.get_pytest_command()** (3 connections) — `scripts/test_runner.py`
- **.__init__()** (3 connections) — `scripts/test_runner.py`
- **.run_all_tests()** (3 connections) — `scripts/test_runner.py`
- **.run_coverage_report()** (3 connections) — `scripts/test_runner.py`
- **.run_integration_tests()** (3 connections) — `scripts/test_runner.py`
- **.setup_test_environment()** (3 connections) — `scripts/test_runner.py`
- **.run_e2e_tests()** (2 connections) — `scripts/test_runner.py`
- **.run_unit_tests()** (2 connections) — `scripts/test_runner.py`
- **Path** (1 connections)
- **Verify test database configuration. Note: For PostgreSQL databases, schema is…** (1 connections) — `scripts/test_runner.py`
- **Build the pytest command with proper configuration. Args: test_paths: List of…** (1 connections) — `scripts/test_runner.py`
- **# NOTE: Test runner uses minimal structlog configuration for console output** (1 connections) — `scripts/test_runner.py`
- **Run the test suite with proper configuration. Args: test_paths: List of test…** (1 connections) — `scripts/test_runner.py`
- **Run integration tests only.** (1 connections) — `scripts/test_runner.py`
- **Run all tests (unit, integration, but not E2E by default).** (1 connections) — `scripts/test_runner.py`
- **Generate coverage report only.** (1 connections) — `scripts/test_runner.py`
- **Main entry point for the test runner.** (1 connections) — `scripts/test_runner.py`
- **Clean test runner for MythosMUD server tests. This class provides a modern,…** (1 connections) — `scripts/test_runner.py`
- **Initialize the test runner with project root.** (1 connections) — `scripts/test_runner.py`
- **Set up the test environment with proper configuration. Returns: Environment…** (1 connections) — `scripts/test_runner.py`

## Relationships

- [safe_run_static](safe_run_static.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)

## Source Files

- `scripts/test_runner.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*