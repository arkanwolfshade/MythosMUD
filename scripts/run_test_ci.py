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
        "cd /workspace/client && npm run test:coverage && "
        "cd /workspace/client && npm run test && "
        "cd /workspace && source .venv/bin/activate && "
        "pytest server/tests/ --cov=server --cov-report=xml --cov-report=html "
        "--cov-fail-under=80 -v --tb=short"
    )

    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{PROJECT_ROOT}:/workspace",
            "-w",
            "/workspace",
            ACT_RUNNER_IMAGE,
            "bash",
            "-c",
            docker_cmd,
        ],
        check=True,
    )
