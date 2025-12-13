#!/usr/bin/env python3
"""Run CI test suite with cross-platform CI detection."""

import json
import os
import subprocess
import sys
import time

# Configure stdout/stderr encoding for Windows to handle Unicode characters
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        # Python < 3.7 doesn't have reconfigure, use buffer directly
        pass

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

    # Check if Node.js and npm are available, and install client dependencies if needed
    client_dir = os.path.join(PROJECT_ROOT, "client")
    node_modules_dir = os.path.join(client_dir, "node_modules")

    # Check if Node.js is available
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
        subprocess.run(["npm", "--version"], capture_output=True, check=True)
        print("Node.js and npm are available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("WARNING: Node.js/npm not found. Skipping client tests.")
        print("Client tests should be run in the frontend CI job instead.")
    else:
        # Install client dependencies if node_modules doesn't exist
        if not os.path.exists(node_modules_dir):
            print(f"Installing client dependencies in {client_dir}...")
            subprocess.run(
                ["npm", "ci"],
                cwd=client_dir,
                check=True,
            )
        else:
            print("Client dependencies already installed")

        # Client tests with coverage
        subprocess.run(
            ["npm", "run", "test:coverage"],
            cwd=client_dir,
            check=True,
        )
        # Client E2E tests
        subprocess.run(
            ["npm", "run", "test"],
            cwd=client_dir,
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

    # #region agent log
    log_path = os.path.join(PROJECT_ROOT, ".cursor", "debug.log")
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_docker_prep",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:75",
                        "message": "Starting Docker CI test execution",
                        "data": {"project_root": PROJECT_ROOT, "platform": sys.platform},
                        "sessionId": "debug-session",
                        "runId": "docker-ci",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (RuntimeError, TypeError):
        pass  # Ignore logging errors
    # #endregion

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
        # Clean up coverage directory contents before running tests to avoid EBUSY errors
        # The directory is a Docker volume mount, so we can't remove the directory itself,
        # but we can clear its contents. This prevents vitest from failing when it tries
        # to clean the directory and encounters locked files from previous runs.
        "mkdir -p /workspace/client/coverage && "
        "find /workspace/client/coverage -mindepth 1 -delete 2>/dev/null || true && "
        "cd /workspace/client && npm run test:coverage && "
        "cd /workspace/client && npm run test && "
        # Use .venv from Docker volume (preserved from build, not overwritten by mount)
        "cd /workspace && source .venv/bin/activate && "
        "pytest server/tests/ --cov=server --cov-report=xml --cov-report=html "
        "--cov-fail-under=80 -v --tb=short"
    )

    # #region agent log
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_docker_cmd",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:108",
                        "message": "Executing Docker command with coverage cleanup",
                        "data": {"docker_cmd_preview": docker_cmd[:200] + "..."},
                        "sessionId": "debug-session",
                        "runId": "docker-ci",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (RuntimeError, TypeError):
        pass  # Ignore logging errors
    # #endregion

    # Mount workspace from host, but use Docker volumes to override dependencies and caches
    # This ensures we only use source code from the host, not host's .venv, node_modules, or caches
    # Docker volumes take precedence over bind mounts, so host dependencies are ignored
    # This avoids Windows filesystem I/O issues and ensures Linux-specific dependencies work correctly
    result = subprocess.run(
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
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",  # Replace un-decodable bytes with replacement character instead of failing
    )

    # #region agent log
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_docker_result",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:140",
                        "message": "Docker command execution completed",
                        "data": {
                            "returncode": result.returncode,
                            "stdout_length": len(result.stdout),
                            "stderr_length": len(result.stderr),
                            "has_ebusy_error": "EBUSY" in result.stderr or "EBUSY" in result.stdout,
                        },
                        "sessionId": "debug-session",
                        "runId": "docker-ci",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (RuntimeError, TypeError):
        pass  # Ignore logging errors
    # #endregion

    if result.returncode != 0:
        # Safely print output, handling Unicode characters on Windows
        try:
            print(result.stdout)
        except UnicodeEncodeError:
            # Fallback: write directly to buffer with UTF-8
            sys.stdout.buffer.write(result.stdout.encode("utf-8", errors="replace"))
            sys.stdout.buffer.write(b"\n")
        try:
            print(result.stderr, file=sys.stderr)
        except UnicodeEncodeError:
            # Fallback: write directly to buffer with UTF-8
            sys.stderr.buffer.write(result.stderr.encode("utf-8", errors="replace"))
            sys.stderr.buffer.write(b"\n")
        sys.exit(result.returncode)
