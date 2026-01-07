#!/usr/bin/env python3
"""Test script to verify venv Python detection logic."""

import os
import sys

# Simulate what happens in CI
PROJECT_ROOT = os.getcwd()
IN_CI = True

print("=== Testing venv Python detection logic ===\n")

# Check what sys.executable is
print(f"1. sys.executable: {sys.executable}")
print(f"   os.path.abspath(sys.executable): {os.path.abspath(sys.executable)}")
print(f"   os.path.realpath(sys.executable): {os.path.realpath(sys.executable)}")

# Check for .venv-ci/bin/python
venv_name = ".venv-ci"
venv_path = os.path.join(PROJECT_ROOT, venv_name, "bin", "python")

print(f"\n2. Looking for venv Python: {venv_path}")

if os.path.exists(venv_path):
    venv_path_abs = os.path.abspath(venv_path)
    venv_path_real = os.path.realpath(venv_path)

    print(f"   Found! abs: {venv_path_abs}")
    print(f"          real: {venv_path_real}")
    print(f"   Is symlink: {os.path.islink(venv_path)}")

    # Check if sys.executable matches
    print("\n3. Comparison:")
    print(f"   sys.executable == venv_path_abs: {sys.executable == venv_path_abs}")
    print(f"   os.path.abspath(sys.executable) == venv_path_abs: {os.path.abspath(sys.executable) == venv_path_abs}")
    print(
        f"   os.path.realpath(sys.executable) == venv_path_real: {os.path.realpath(sys.executable) == venv_path_real}"
    )

    # What the script will use
    if IN_CI and os.path.abspath(sys.executable) == venv_path_abs:
        python_exe = sys.executable
        print(f"\n   ✓ Will use sys.executable: {python_exe}")
    else:
        python_exe = venv_path_abs
        print(f"\n   ✗ Will use venv_path: {python_exe}")

    # Check if pytest is available
    import subprocess

    try:
        result = subprocess.run(
            [python_exe, "-c", "import pytest; print(pytest.__version__)"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            print(f"   ✓ pytest available: {result.stdout.strip()}")
        else:
            print(f"   ✗ pytest NOT available: {result.stderr}")
    except Exception as e:
        print(f"   ✗ Error checking pytest: {e}")
else:
    print("   ✗ Venv Python not found")
