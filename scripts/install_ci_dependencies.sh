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

# Check if venv Python is a symlink (uv venv may create symlinks)
if [ -L "$PYTHON_EXE" ]; then
    echo "WARNING: Venv Python is a symlink, using activation to ensure proper isolation"
    USE_EXPLICIT_PYTHON="false"
fi

if [ "$USE_EXPLICIT_PYTHON" = "true" ]; then
    echo "Installing dependencies with explicit --python flag..."
    uv pip install --python "$PYTHON_EXE" -e .
    uv pip install --python "$PYTHON_EXE" -e ".[dev]"
    uv pip install --python "$PYTHON_EXE" pytest-mock>=3.14.0 pytest-xdist>=3.8.0
else
    echo "Installing dependencies with venv activation (ensures proper site-packages isolation)..."
    source "$VENV_NAME/bin/activate"
    # Verify we're using the venv Python
    echo "Active Python: $(which python)"
    echo "Python executable: $(python -c 'import sys; print(sys.executable)')"
    echo "VIRTUAL_ENV: $VIRTUAL_ENV"

    # Check if pip is available in the venv
    if ! python -m pip --version >/dev/null 2>&1; then
        echo "Installing pip into venv..."
        uv pip install --python "$PYTHON_EXE" pip
    fi

    # Use python -m pip to ensure packages install into the venv's site-packages
    # This is more reliable when the venv Python is a symlink
    python -m pip install --upgrade pip
    python -m pip install -e .
    python -m pip install -e ".[dev]"
    python -m pip install pytest-mock>=3.14.0 pytest-xdist>=3.8.0
    deactivate
fi

# Verify pytest is installed in the venv's own site-packages
echo "Verifying pytest installation..."
# Use the venv Python directly to check its site-packages
VENV_SITE_PACKAGES=$("$PYTHON_EXE" -c "import site; print(site.getsitepackages()[0] if site.getsitepackages() else site.getusersitepackages())")
echo "Venv site-packages: $VENV_SITE_PACKAGES"
echo "Python executable: $PYTHON_EXE"

# Check if this is the venv's own site-packages or the base Python's
# The venv's site-packages should be inside the venv directory
if [[ "$VENV_SITE_PACKAGES" != *"$VENV_NAME"* ]] && [ -L "$PYTHON_EXE" ]; then
    echo "WARNING: Site-packages is not in venv directory, may be using base Python's site-packages"
    echo "This can happen when venv Python is a symlink. Checking venv's own site-packages..."
    # Try to find the venv's actual site-packages
    if [ -d "$VENV_NAME/lib" ]; then
        VENV_LIB_DIR=$(find "$VENV_NAME/lib" -type d -name "site-packages" 2>/dev/null | head -1)
        if [ -n "$VENV_LIB_DIR" ]; then
            echo "Found venv's actual site-packages: $VENV_LIB_DIR"
            VENV_SITE_PACKAGES="$VENV_LIB_DIR"
        fi
    fi
fi

if [ -d "$VENV_SITE_PACKAGES/pytest" ]; then
    echo "✓ pytest found in venv site-packages"
else
    echo "ERROR: pytest NOT found in venv site-packages: $VENV_SITE_PACKAGES/pytest"
    echo "Listing site-packages contents:"
    ls -la "$VENV_SITE_PACKAGES" | head -20
    echo ""
    echo "Checking if venv has its own site-packages directory:"
    if [ -d "$VENV_NAME/lib" ]; then
        find "$VENV_NAME/lib" -type d -name "site-packages" -exec ls -la {} \; 2>/dev/null | head -20
    fi
    exit 1
fi

# Verify pytest can be imported using the venv Python
"$PYTHON_EXE" -c "import pytest; print(f'pytest version: {pytest.__version__}')" || {
    echo "ERROR: pytest import failed"
    echo "This suggests packages were installed in the wrong location"
    exit 1
}

echo "✓ All dependencies installed successfully"
