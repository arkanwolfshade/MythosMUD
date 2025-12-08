# Testing Guide for MythosMUD

## Quick Start

### Running Tests

```powershell
# Daily development - fast unit tests (~5-7 min)
make test

# Full suite - all tests including slow ones (~30 min)
make test-comprehensive

# Coverage report
make test-coverage

# Slow tests only (performance, integration)
make test-slow
```

### Fresh Session Testing (For bcrypt-dependent modules)

Some modules import `server.models.user` which triggers bcrypt initialization. Due to PyO3 limitations, bcrypt can only be initialized once per Python interpreter. If you encounter this error:

```
ImportError: PyO3 modules compiled for CPython 3.8 or older may only be initialized once per interpreter process
```

**Solution: Run tests in a fresh terminal session:**

```powershell
# Open NEW PowerShell terminal, then run:
uv run pytest server/tests/unit/api/test_metrics.py -v --cov=server.api.metrics --cov-report=term-missing

# Or run all unit tests in isolated workers:
uv run pytest server/tests/unit/ -n auto -v
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

The Makefile already uses `pytest-xdist` (`-n auto`) for parallelization:

- **`make test`**: Daily development suite (excludes slow/e2e, parallel)
- **`make test-comprehensive`**: Full suite via Docker (fresh environment)
- **`make test-coverage`**: Generate coverage reports
- **`make test-slow`**: Slow tests only
- **`make test-e2e`**: End-to-end tests

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

- **Overall Coverage**: 80% minimum (enforced in CI), 82%+ target
- **Critical Coverage**: 98% minimum (security, core features)
- **Test Quality**: Focus on high-value tests preventing regressions

### Test Markers

- `@pytest.mark.slow` - Slow tests (>1s), excluded from `make test`
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

## bcrypt PyO3 Limitation - Technical Details

### Why This Happens

1. bcrypt uses PyO3 (Rust-Python bindings)
2. PyO3 modules can only be initialized once per interpreter
3. Running multiple test files sequentially re-imports bcrypt
4. Second import fails with PyO3 initialization error

### Workarounds

**Option 1: Fresh Terminal (Simplest)**
```powershell
# Close current terminal, open new one
uv run pytest server/tests/unit/api/test_metrics.py -v
```

**Option 2: Run Specific Tests First (In New Session)**
```powershell
# In fresh terminal, run bcrypt-dependent tests FIRST
uv run pytest server/tests/unit/api/ server/tests/unit/commands/test_utility_commands.py -v
```

**Option 3: Use Docker (Most Isolated)**
```powershell
make test-comprehensive  # Runs in fresh Docker container
```

**Option 4: Pytest-xdist with Forked Mode (Linux/Mac only)**
```bash
# Note: --forked not available on Windows
pytest -n auto --forked
```

### Prevention During Development

- Test bcrypt-dependent modules in fresh sessions
- Run infrastructure/utility tests before API/auth tests
- Use `make test-comprehensive` for final validation (Docker isolation)

## Test Organization

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

## Common Issues

### Issue: Tests hang indefinitely
**Solution**: Check for running server instances, stop with `./scripts/stop_server.ps1`

### Issue: Database connection errors
**Solution**: Run `make check-postgresql` and `make setup-postgresql-test-db`

### Issue: Import errors
**Solution**: Ensure virtual environment is activated: `uv sync`

### Issue: Slow test runs
**Solution**: Use `make test` (excludes slow tests) instead of `make test-comprehensive`
