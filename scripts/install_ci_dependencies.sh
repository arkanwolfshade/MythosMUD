#!/bin/bash
# Install CI dependencies consistently across Docker, GitHub Actions, and local test-ci
# This ensures all environments use the same Python environment and dependencies

set -euo pipefail

# Determine venv name (default to .venv-ci for CI, .venv for local)
VENV_NAME="${VENV_NAME:-.venv-ci}"

# Determine if we should use explicit --python flag or activation
# Explicit flag is more reliable in CI environments
USE_EXPLICIT_PYTHON="${USE_EXPLICIT_PYTHON:-true}"

echo "Installing CI dependencies..."
echo "Venv name: $VENV_NAME"
echo "Use explicit Python: $USE_EXPLICIT_PYTHON"

# Create venv if it doesn't exist
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment: $VENV_NAME"
    uv venv "$VENV_NAME"
else
    echo "Virtual environment already exists: $VENV_NAME"
fi

# Determine Python executable path
if [ "$(uname -s)" = "Linux" ] || [ "$(uname -s)" = "Darwin" ]; then
    PYTHON_EXE="$VENV_NAME/bin/python"
else
    # Windows
    PYTHON_EXE="$VENV_NAME/Scripts/python.exe"
fi

# Make path absolute
PYTHON_EXE=$(cd "$(dirname "$PYTHON_EXE")" && pwd)/$(basename "$PYTHON_EXE")

if [ "$USE_EXPLICIT_PYTHON" = "true" ]; then
    echo "Installing dependencies with explicit --python flag..."
    uv pip install --python "$PYTHON_EXE" -e .
    uv pip install --python "$PYTHON_EXE" -e ".[dev]"
    uv pip install --python "$PYTHON_EXE" pytest-mock>=3.14.0 pytest-xdist>=3.8.0
else
    echo "Installing dependencies with venv activation..."
    source "$VENV_NAME/bin/activate"
    uv pip install -e .
    uv pip install -e ".[dev]"
    uv pip install pytest-mock>=3.14.0 pytest-xdist>=3.8.0
fi

# Verify pytest is installed
echo "Verifying pytest installation..."
VENV_SITE_PACKAGES=$("$PYTHON_EXE" -c "import site; print(site.getsitepackages()[0] if site.getsitepackages() else site.getusersitepackages())")
echo "Venv site-packages: $VENV_SITE_PACKAGES"

if [ -d "$VENV_SITE_PACKAGES/pytest" ]; then
    echo "✓ pytest found in venv site-packages"
else
    echo "ERROR: pytest NOT found in venv site-packages: $VENV_SITE_PACKAGES/pytest"
    echo "Listing site-packages contents:"
    ls -la "$VENV_SITE_PACKAGES" | head -20
    exit 1
fi

# Verify pytest can be imported
"$PYTHON_EXE" -c "import pytest; print(f'pytest version: {pytest.__version__}')" || {
    echo "ERROR: pytest import failed"
    exit 1
}

echo "✓ All dependencies installed successfully"
