#!/usr/bin/env python3
"""Run CI test suite with cross-platform CI detection."""

import os
import subprocess
import sys

# Determine project root
PROJECT_ROOT = os.getcwd()
if "MythosMUD-" in PROJECT_ROOT:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

# Check if we're in CI environment
CI = os.getenv("CI")
GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS")
IN_CI = bool(CI or GITHUB_ACTIONS)

if IN_CI:
    print("Running CI test suite directly (already in CI environment)...")
    # Client tests with coverage
    subprocess.run(
        ["npm", "run", "test:coverage"],
        cwd=os.path.join(PROJECT_ROOT, "client"),
        check=True,
    )
    # Client E2E tests
    subprocess.run(
        ["npm", "run", "test"],
        cwd=os.path.join(PROJECT_ROOT, "client"),
        check=True,
    )
    # Server tests with coverage
    # Use Python from .venv-ci to run pytest as a module (cross-platform)
    if sys.platform == "win32":
        python_exe = os.path.join(PROJECT_ROOT, ".venv-ci", "Scripts", "python.exe")
    else:
        python_exe = os.path.join(PROJECT_ROOT, ".venv-ci", "bin", "python")

    subprocess.run(
        [
            python_exe,
            "-m",
            "pytest",
            "server/tests/",
            "--cov=server",
            "--cov-report=xml",
            "--cov-report=html",
            "--cov-fail-under=80",
            "-v",
            "--tb=short",
        ],
        cwd=PROJECT_ROOT,
        check=True,
    )
else:
    print("Building Docker runner image (this ensures dependencies are up-to-date)...")
    ACT_RUNNER_IMAGE = "mythosmud-gha-runner:latest"
    ACT_RUNNER_DOCKERFILE = "Dockerfile.github-runner"

    subprocess.run(
        [
            "docker",
            "build",
            "--pull",
            "-t",
            ACT_RUNNER_IMAGE,
            "-f",
            ACT_RUNNER_DOCKERFILE,
            ".",
        ],
        cwd=PROJECT_ROOT,
        check=True,
    )

    print("Running CI test suite in Docker (coverage enforced)...")
    print("Starting PostgreSQL service in container...")

    # Convert Windows path to Docker-compatible path
    workspace_path = PROJECT_ROOT
    if sys.platform == "win32":
        # Convert Windows path to WSL/Docker format if needed
        # For Docker Desktop on Windows, we can use the path as-is with proper escaping
        workspace_path = PROJECT_ROOT.replace("\\", "/")

    docker_cmd = (
        "service postgresql start && sleep 3 && "
        # Install npm dependencies in container (node_modules uses Docker volume, not Windows mount)
        # This ensures Linux-specific optional dependencies are installed correctly
        "cd /workspace/client && npm install && "
        "cd /workspace/client && npm run test:coverage && "
        "cd /workspace/client && npm run test && "
        # Use .venv from Docker volume (preserved from build, not overwritten by mount)
        "cd /workspace && source .venv/bin/activate && "
        "pytest server/tests/ --cov=server --cov-report=xml --cov-report=html "
        "--cov-fail-under=80 -v --tb=short"
    )

    # Mount workspace from host, but use Docker volumes to override dependencies and caches
    # This ensures we only use source code from the host, not host's .venv, node_modules, or caches
    # Docker volumes take precedence over bind mounts, so host dependencies are ignored
    # This avoids Windows filesystem I/O issues and ensures Linux-specific dependencies work correctly
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            # Mount workspace (source code only - dependencies overridden by volumes below)
            "-v",
            f"{PROJECT_ROOT}:/workspace",
            # Override host dependencies with Docker volumes (Linux-specific)
            "-v",
            "mythosmud-node-modules:/workspace/client/node_modules",
            "-v",
            "mythosmud-venv:/workspace/.venv",
            # Override host caches and build artifacts with Docker volumes
            "-v",
            "mythosmud-npm-cache:/root/.npm",
            "-v",
            "mythosmud-pytest-cache:/workspace/.pytest_cache",
            "-v",
            "mythosmud-coverage:/workspace/htmlcov",
            "-v",
            "mythosmud-client-coverage:/workspace/client/coverage",
            "-v",
            "mythosmud-client-dist:/workspace/client/dist",
            "-w",
            "/workspace",
            ACT_RUNNER_IMAGE,
            "bash",
            "-c",
            docker_cmd,
        ],
        check=True,
    )
