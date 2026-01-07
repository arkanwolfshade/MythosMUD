# CI Environment Alignment

This document describes how we've aligned the Docker, GitHub Actions, and local `make test-ci` environments to ensure consistent test execution across all platforms.

## Problem

Previously, there were inconsistencies between:
- **Dockerfile.github-runner**: Used `.venv`, activation-based installation, missing `pytest-xdist`
- **GitHub Actions workflow**: Used `.venv-ci`, explicit `--python` flag, included `pytest-xdist`
- **Local `make test-ci`**: Used system Python, no venv detection

This led to:
- Tests passing locally but failing in CI
- Different dependency versions between environments
- Difficulty reproducing CI failures locally

## Solution

### 1. Shared Dependency Installation Script

Created `scripts/install_ci_dependencies.sh` that:
- Uses configurable venv name (defaults to `.venv-ci` for CI)
- Supports both explicit `--python` flag and activation-based installation
- Verifies pytest installation by checking site-packages
- Ensures all environments install the same dependencies:
  - `pytest-mock>=3.14.0`
  - `pytest-xdist>=3.8.0`

### 2. Dockerfile Alignment

**Before:**
```dockerfile
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -e . && \
    uv pip install -e ".[dev]" && \
    uv pip install pytest-mock>=3.14.0
```

**After:**
```dockerfile
RUN VENV_NAME=.venv-ci USE_EXPLICIT_PYTHON=true bash scripts/install_ci_dependencies.sh
```

**Changes:**
- Uses `.venv-ci` to match GitHub Actions
- Uses explicit `--python` flag for reliability
- Includes `pytest-xdist>=3.8.0`
- Uses shared installation script

### 3. GitHub Actions Alignment

**Before:**
```yaml
- name: Install dependencies
  run: |
    uv venv .venv-ci
    uv pip install --python .venv-ci/bin/python -e .
    # ... many lines of verification
```

**After:**
```yaml
- name: Install dependencies
  run: |
    VENV_NAME=.venv-ci USE_EXPLICIT_PYTHON=true bash scripts/install_ci_dependencies.sh
```

**Changes:**
- Uses shared installation script
- Same verification logic as Docker
- Consistent with Docker environment

### 4. Makefile Alignment

**Before:**
```makefile
test-ci:
	$(PYTHON) scripts/run_test_ci.py
```

**After:**
```makefile
test-ci:
	@# run_test_ci.py automatically detects and uses .venv-ci or .venv if available
	@# This ensures local test-ci matches CI environment behavior
	$(PYTHON) scripts/run_test_ci.py
```

**Changes:**
- `run_test_ci.py` already handles venv detection (`.venv-ci` first, then `.venv`)
- Works on both Windows and Unix
- Automatically uses venv Python when available

## How It Works

### Venv Detection Priority

`scripts/run_test_ci.py` checks for venvs in this order:
1. `.venv-ci` (CI environment)
2. `.venv` (local development)
3. Falls back to `sys.executable` if no venv found

### Installation Method

The shared script supports two modes:
- **Explicit Python flag** (`USE_EXPLICIT_PYTHON=true`): More reliable in CI, used by Docker and GitHub Actions
- **Venv activation** (`USE_EXPLICIT_PYTHON=false`): Can be used for local development if preferred

### Verification

All environments verify pytest installation by:
1. Checking if pytest directory exists in venv's site-packages
2. Attempting to import pytest and print version
3. Listing site-packages contents if verification fails (for debugging)

## Benefits

1. **Consistency**: All environments use the same venv name, dependencies, and installation method
2. **Reproducibility**: Local `make test-ci` now matches CI behavior
3. **Maintainability**: Single source of truth for dependency installation
4. **Debugging**: Better error messages when dependencies are missing

## Usage

### Local Development

```bash
# Install dependencies (creates .venv-ci to match CI)
VENV_NAME=.venv-ci USE_EXPLICIT_PYTHON=true bash scripts/install_ci_dependencies.sh

# Run tests (automatically uses .venv-ci if available)
make test-ci
```

### Docker

The Dockerfile automatically uses the shared script, no changes needed.

### GitHub Actions

The workflow automatically uses the shared script, no changes needed.

## Future Improvements

1. Consider using `uv sync` instead of `uv pip install` for better dependency resolution
2. Add dependency version pinning to ensure exact version matches
3. Consider using `uv`'s project environment feature when it's more stable
