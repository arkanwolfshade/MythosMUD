# Testing Guide for MythosMUD

**Version 1.1.0** · MythosMUD · 2026-08-03

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Quick Start

**[NOTE]**

### Running Tests

```powershell
# Daily development - client + server (excludes integration)

make test

# Coverage report

make test-coverage

# CI-style suite (coverage thresholds; Docker locally)

make test-ci

# Playwright client E2E

make test-client-e2e

# Playwright + server integration (needs care with data)

make test-playwright
```

### Fresh Session Testing (For bcrypt-dependent modules)

Some modules import `server.models.user` which triggers bcrypt initialization. Due to PyO3 limitations, bcrypt can only
be initialized once per Python interpreter. If you encounter this error:

```
ImportError: PyO3 modules compiled for CPython 3.8 or older may only be initialized once per interpreter process
```

### Solution: Run tests in a fresh terminal session

```powershell
# Open NEW PowerShell terminal, then run

uv run pytest server/tests/unit/api/test_metrics.py -v --cov=server.api.metrics --cov-report=term-missing

# Or run the whole unit tier

uv run pytest server/tests/unit/ -v
```

### Affected Modules

These modules require fresh sessions after other tests have run:

- `server/api/metrics.py`
- `server/api/containers.py`
- `server/api/real_time.py`
- `server/auth/invites.py`
- `server/commands/utility_commands.py`
- `server/npc/spawning_service.py`

### Makefile Targets

**`make test`**: Client unit + server (excludes `integration` marker)

**`make test-coverage`**: Client and server coverage reports

**`make test-ci`**: CI-style suite with coverage thresholds (`scripts/run_test_ci.py`)

**`make test-client-e2e`**: Playwright E2E (`make test-e2e` is an alias)

**`make test-playwright`**: Client E2E + server integration helpers

**`make test-comprehensive`**: Legacy alias for `make test-ci`

### Running Individual Test Files

```powershell
# Single file

uv run pytest server/tests/unit/path/to/test_file.py -v

# Single file with coverage

uv run pytest server/tests/unit/path/to/test_file.py --cov=server.module.path --cov-report=term-missing

# Single test class

uv run pytest server/tests/unit/path/to/test_file.py::TestClassName -v

# Single test method

uv run pytest server/tests/unit/path/to/test_file.py::TestClassName::test_method_name -v
```

### Coverage Requirements

**Global floor (`.coveragerc` `fail_under`)**: 70% line coverage for measured server code

**Normal files**: 70% minimum per file (`scripts/check_coverage_thresholds.py`, hard-fail)

**Critical files**: 90% minimum per listed path (or a justified lowered threshold in
`CRITICAL_FILES` / `docs/PYTHON_COVERAGE_STATUS.md`)

**Test Quality**: Focus on high-value tests preventing regressions

Keep `CRITICAL_FILES` in `scripts/check_coverage_thresholds.py` and
`scripts/analyze_coverage_gaps.py` in sync when editing the list.

### Test Markers

`@pytest.mark.slow` - Slow tests (>1s), excluded from `make test`

- `@pytest.mark.e2e` - End-to-end tests, excluded from `make test`
- `@pytest.mark.asyncio` - Async tests

### Debugging Tests

```powershell
# Stop on first failure

uv run pytest -x

# Show full traceback

uv run pytest --tb=long

# Show print statements

uv run pytest -s

# Run with verbose output

uv run pytest -v

# Run specific test with debugging

uv run pytest server/tests/unit/test_file.py::test_name -v -s --tb=long
```

## 2. bcrypt PyO3 Limitation - Technical Details

**[NOTE]**

### Why This Happens

1. bcrypt uses PyO3 (Rust-Python bindings)
2. PyO3 modules can only be initialized once per interpreter
3. Running multiple test files sequentially re-imports bcrypt
4. Second import fails with PyO3 initialization error

### Workarounds

### Option 1: Fresh Terminal (Simplest)

```powershell
# Close current terminal, open new one

uv run pytest server/tests/unit/api/test_metrics.py -v
```

### Option 2: Run Specific Tests First (In New Session)

```powershell
# In fresh terminal, run bcrypt-dependent tests FIRST

uv run pytest server/tests/unit/api/ server/tests/unit/commands/test_utility_commands.py -v
```

### Option 3: Use CI-style suite (Most Isolated)

```powershell
make test-ci  # Docker locally when not already in CI
```

### Prevention During Development

Test bcrypt-dependent modules in fresh sessions

- Run infrastructure/utility tests before API/auth tests
- Use `make test-ci` for final validation (Docker isolation when local)

## 3. Test Organization

**[NOTE]**

```
server/tests/
├── unit/                    # Unit tests (fast, isolated)
│   ├── api/                # API endpoint tests
│   ├── caching/            # Cache service tests
│   ├── commands/           # Command handler tests
│   ├── infrastructure/     # Infrastructure tests
│   ├── realtime/           # Real-time connection tests
│   └── utils/              # Utility function tests
├── integration/             # Integration tests (slow)
├── performance/             # Performance benchmarks (slow)
├── e2e/                     # End-to-end tests (slow)
└── verification/            # System verification tests
```

## 4. Common Issues

**[NOTE]**

### Issue: Tests hang indefinitely

**Solution**: Check for running server instances, stop with `./scripts/stop_server.ps1`

### Issue: Database connection errors

**Solution**: Run `make check-postgresql` and `make setup-postgresql-test-db`

### Issue: Import errors

**Solution**: Ensure virtual environment is activated: `uv sync`

### Issue: Slow test runs

**Solution**: Use `make test` for the daily suite; use `make test-ci` for fuller CI validation

## 5. Markers and isolation (greenfield)

**[SPEC]**

- Preferred entrypoints: `make test`, `make test-ci`, `make test-coverage` (repo root only)
- Markers: `unit`, `integration`, `e2e`, `slow`
- Never start the MythosMUD server inside tests
- The suite runs serially (see #724: pytest-xdist removed entirely -- its worker
  restart/shutdown protocol produced false "worker crashed" reports, an unresolved upstream
  xdist/execnet gap)
- Unit tier: no real network/DB/filesystem writes; use fakes/mocks
- Integration tier: ephemeral Postgres; truncate/rollback between tests
- See also `server/tests/README.md`

**[NOTE]**
Merged from archived root greenfield notes (`docs/archive/TESTING_GREENFIELD.md`).

## 6. Changelog

**[SPEC]**

| Version | Date       | Change                                                       |
| ------- | ---------- | ------------------------------------------------------------ |
| 1.1.0   | 2026-08-03 | Align Makefile targets with real `test-ci` / E2E names       |
| 1.0.0   | 2026-07-30 | Initial HADS structural conversion; merge greenfield markers |
