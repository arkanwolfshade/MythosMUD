#!/usr/bin/env python3
"""Run CI test suite with cross-platform CI detection."""

import json
import os
import queue
import subprocess
import sys
import threading
import time

from utils.safe_subprocess import safe_run_static

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
    print("NOTE: Frontend tests are run in the 'React Client' CI job, not here.")
    print("This job only runs backend Python tests.")

    # Server tests with coverage
    # Use Python from .venv-ci to run pytest as a module (cross-platform)
    if sys.platform == "win32":
        python_exe = os.path.join(PROJECT_ROOT, ".venv-ci", "Scripts", "python.exe")
    else:
        python_exe = os.path.join(PROJECT_ROOT, ".venv-ci", "bin", "python")

    # Set environment variables to prevent output buffering issues in CI/Docker
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    # #region agent log
    log_path = os.path.join(PROJECT_ROOT, ".cursor", "debug.log")
    try:
        # Check password env var without storing the actual value to avoid CodeQL alert
        pw_exists = "MYTHOSMUD_ADMIN_PASSWORD" in env
        pw_value = env.get("MYTHOSMUD_ADMIN_PASSWORD", "")
        pw_set = pw_value != "" and pw_value != "NOT_SET"
        pw_length = len(pw_value) if pw_set else 0
        # Clear the variable to avoid storing sensitive data
        pw_value = None
        del pw_value
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_ci_env_check",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:44",
                        "message": "CI environment check - MYTHOSMUD_ADMIN_PASSWORD",
                        "data": {
                            "env_var_exists": pw_exists,
                            "env_var_set": pw_set,
                            "env_var_length": pw_length,
                            "in_ci": IN_CI,
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-env-check",
                        "hypothesisId": "F",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    # #region agent log
    log_path = os.path.join(PROJECT_ROOT, ".cursor", "debug.log")
    try:
        # Check if pytest-xdist is installed
        import importlib.util

        xdist_path = importlib.util.find_spec("xdist")
        pytest_xdist_installed = xdist_path is not None
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_check_xdist",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:47",
                        "message": "Checking if pytest-xdist is installed",
                        "data": {
                            "pytest_xdist_installed": pytest_xdist_installed,
                            "xdist_path": str(xdist_path) if xdist_path else None,
                            "python_exe": python_exe,
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-check",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    # #region agent log
    try:
        # Check installed packages
        result = safe_run_static(
            python_exe,
            "-m",
            "pip",
            "list",
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
            env=env,
            check=False,  # Don't raise on error, just log the output
        )
        installed_packages = result.stdout
        has_pytest_xdist = "pytest-xdist" in installed_packages
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_pip_list",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:75",
                        "message": "Checking installed packages via pip list",
                        "data": {
                            "has_pytest_xdist": has_pytest_xdist,
                            "pip_list_output_preview": installed_packages[:500],
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-check",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    # #region agent log
    try:
        # Check pytest plugins
        result = safe_run_static(
            python_exe,
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
            env=env,
            check=False,  # Don't raise on error, just log the output
        )
        pytest_plugins = result.stdout + result.stderr
        has_xdist_plugin = "xdist" in pytest_plugins or "pytest-xdist" in pytest_plugins
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_pytest_plugins",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:100",
                        "message": "Checking pytest plugins",
                        "data": {
                            "has_xdist_plugin": has_xdist_plugin,
                            "pytest_output_preview": pytest_plugins[:500],
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-check",
                        "hypothesisId": "B",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    # #region agent log
    try:
        # Read pytest.ini to check for -n flag
        pytest_ini_path = os.path.join(PROJECT_ROOT, "server", "pytest.ini")
        with open(pytest_ini_path, encoding="utf-8") as f:
            pytest_ini_content = f.read()
        has_n_auto = "-n auto" in pytest_ini_content or "-n" in pytest_ini_content
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_pytest_ini",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:125",
                        "message": "Checking pytest.ini for -n flag",
                        "data": {
                            "has_n_auto": has_n_auto,
                            "pytest_ini_preview": pytest_ini_content[:500],
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-check",
                        "hypothesisId": "C",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    # Run tests with coverage
    # #region agent log
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_pytest_start",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:150",
                        "message": "Starting pytest execution",
                        "data": {
                            "pytest_command": [
                                python_exe,
                                "-m",
                                "pytest",
                                "server/tests/",
                                "--cov=server",
                                "--cov-report=xml",
                                "--cov-report=html",
                                "--cov-config=.coveragerc",
                                "-v",
                                "--tb=short",
                            ],
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-check",
                        "hypothesisId": "D",
                    }
                )
                + "\n"
            )
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion
    safe_run_static(
        python_exe,
        "-m",
        "pytest",
        "server/tests/",
        "--cov=server",
        "--cov-report=xml",
        "--cov-report=html",
        "--cov-config=.coveragerc",
        "-v",
        "--tb=short",
        cwd=PROJECT_ROOT,
        check=True,
        env=env,
    )

    # Check per-file thresholds
    check_script = os.path.join(PROJECT_ROOT, "scripts", "check_coverage_thresholds.py")
    safe_run_static(
        python_exe,
        check_script,
        cwd=PROJECT_ROOT,
        check=True,
        env=env,
    )
else:
    # #region agent log
    log_path = os.path.join(PROJECT_ROOT, ".cursor", "debug.log")
    try:
        # Check password env var without storing the actual value to avoid CodeQL alert
        pw_exists = "MYTHOSMUD_ADMIN_PASSWORD" in os.environ
        pw_value = os.environ.get("MYTHOSMUD_ADMIN_PASSWORD", "")
        pw_set = pw_value != "" and pw_value != "NOT_SET"
        pw_length = len(pw_value) if pw_set else 0
        # Clear the variable to avoid storing sensitive data
        pw_value = None
        del pw_value
        # Check for .env files
        env_files = []
        for env_file in [".env", ".env.local", "server/tests/.env.unit_test"]:
            env_path = os.path.join(PROJECT_ROOT, env_file)
            if os.path.exists(env_path):
                env_files.append(env_file)
        with open(log_path, "a", encoding="utf-8") as f:
            log_entry = json.dumps(
                {
                    "id": f"log_{int(time.time())}_local_env_check",
                    "timestamp": int(time.time() * 1000),
                    "location": "run_test_ci.py:240",
                    "message": "Local environment check - MYTHOSMUD_ADMIN_PASSWORD",
                    "data": {
                        "env_var_exists": pw_exists,
                        "env_var_set": pw_set,
                        "env_var_length": pw_length,
                        "env_files_found": env_files,
                        "in_ci": IN_CI,
                    },
                    "sessionId": "debug-session",
                    "runId": "local-env-check",
                    "hypothesisId": "G",
                }
            )
            f.write(log_entry + "\n")
    except (OSError, TypeError, ValueError):
        pass  # Ignore logging errors (file I/O or JSON serialization issues)
    # #endregion

    print("Building Docker runner image (this ensures dependencies are up-to-date)...")
    ACT_RUNNER_IMAGE = "mythosmud-gha-runner:latest"
    ACT_RUNNER_DOCKERFILE = "Dockerfile.github-runner"

    safe_run_static(
        "docker",
        "build",
        "--pull",
        "-t",
        ACT_RUNNER_IMAGE,
        "-f",
        ACT_RUNNER_DOCKERFILE,
        ".",
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
        # Ensure pytest-mock and pytest-xdist are installed in the venv before running tests
        # pytest-xdist is required for -n auto in pytest.ini
        "cd /workspace && source .venv/bin/activate && "
        "uv pip install pytest-mock>=3.14.0 pytest-xdist>=3.8.0 && "
        "PYTHONUNBUFFERED=1 pytest server/tests/ --cov=server --cov-report=xml --cov-report=html "
        "--cov-config=.coveragerc -v --tb=short && "
        "uv run python scripts/check_coverage_thresholds.py"
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

    # #region agent log
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_docker_run_start",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:194",
                        "message": "Starting Docker run command",
                        "data": {"image": ACT_RUNNER_IMAGE},
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
    # Use Popen with real-time output to avoid deadlock from output buffering
    start_time = time.time()
    # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen1
    # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen2
    # Project requires Python >= 3.12, so encoding/errors arguments are available
    process = subprocess.Popen(
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
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,  # Line buffered
    )

    # #region agent log
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_docker_process_created",
                        "timestamp": int(time.time() * 1000),
                        "location": "run_test_ci.py:230",
                        "message": "Docker process created, starting output reading",
                        "data": {"pid": process.pid},
                        "sessionId": "debug-session",
                        "runId": "docker-ci",
                        "hypothesisId": "A",
                    }
                )
                + "\n"
            )
    except (RuntimeError, TypeError):
        pass
    # #endregion

    # Read output line by line to avoid deadlock from output buffering
    # Use a queue and thread to read output with timeout detection
    output_queue = queue.Queue()
    output_lines = []
    last_output_time = time.time()

    def read_output():
        """Read process output in background thread."""
        try:
            for line in process.stdout:
                output_queue.put(("line", line))
        except OSError as e:
            output_queue.put(("error", str(e)))

    reader_thread = threading.Thread(target=read_output, daemon=True)
    reader_thread.start()

    try:
        # #region agent log
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "id": f"log_{int(time.time())}_reading_output_start",
                            "timestamp": int(time.time() * 1000),
                            "location": "run_test_ci.py:282",
                            "message": "Starting to read Docker output",
                            "data": {},
                            "sessionId": "debug-session",
                            "runId": "docker-ci",
                            "hypothesisId": "A",
                        }
                    )
                    + "\n"
                )
        except (RuntimeError, TypeError):
            pass
        # #endregion

        # Read from queue - no timeout, let tests complete naturally
        while True:
            # Check if process finished
            if process.poll() is not None and output_queue.empty():
                break

            try:
                item_type, item = output_queue.get(timeout=1.0)
                if item_type == "line":
                    output_lines.append(item)
                    print(item, end="", flush=True)

                    # #region agent log - Track important milestones
                    if any(
                        keyword in item.lower()
                        for keyword in [
                            "postgresql",
                            "starting",
                            "test:coverage",
                            "pytest",
                            "timeout",
                            "error",
                            "failed",
                        ]
                    ):
                        try:
                            with open(log_path, "a", encoding="utf-8") as f:
                                f.write(
                                    json.dumps(
                                        {
                                            "id": f"log_{int(time.time())}_docker_milestone",
                                            "timestamp": int(time.time() * 1000),
                                            "location": "run_test_ci.py:340",
                                            "message": "Docker output milestone",
                                            "data": {
                                                "line_preview": item[:150].strip(),
                                                "output_lines_count": len(output_lines),
                                            },
                                            "sessionId": "debug-session",
                                            "runId": "docker-ci",
                                            "hypothesisId": "A",
                                        }
                                    )
                                    + "\n"
                                )
                        except (RuntimeError, TypeError):
                            pass
                    # #endregion
                elif item_type == "error":
                    raise OSError(f"Error reading output: {item}")
            except queue.Empty:
                # Check if process is still running
                if process.poll() is not None:
                    # Process finished, drain remaining queue
                    while not output_queue.empty():
                        try:
                            item_type, item = output_queue.get_nowait()
                            if item_type == "line":
                                output_lines.append(item)
                                print(item, end="", flush=True)
                        except queue.Empty:
                            break
                    break
                continue

        returncode = process.returncode if process.poll() is not None else 1
        stdout = "".join(output_lines)
        stderr = ""

        # #region agent log
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "id": f"log_{int(time.time())}_process_complete",
                            "timestamp": int(time.time() * 1000),
                            "location": "run_test_ci.py:380",
                            "message": "Process completed",
                            "data": {
                                "returncode": returncode,
                                "total_output_lines": len(output_lines),
                                "elapsed_time": int(time.time() - start_time),
                            },
                            "sessionId": "debug-session",
                            "runId": "docker-ci",
                            "hypothesisId": "A",
                        }
                    )
                    + "\n"
                )
        except (RuntimeError, TypeError):
            pass
        # #endregion
    except (OSError, KeyboardInterrupt, RuntimeError) as e:
        # #region agent log
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "id": f"log_{int(time.time())}_docker_error",
                            "timestamp": int(time.time() * 1000),
                            "location": "run_test_ci.py:365",
                            "message": "Error reading Docker output",
                            "data": {"error": str(e), "type": type(e).__name__},
                            "sessionId": "debug-session",
                            "runId": "docker-ci",
                            "hypothesisId": "A",
                        }
                    )
                    + "\n"
                )
        except (RuntimeError, TypeError):
            pass
        # #endregion
        process.kill()
        returncode = 1
        stdout = "".join(output_lines)
        stderr = str(e)

    # Create result-like object
    class Result:
        def __init__(self, retcode, stdout_data, stderr_data):
            self.returncode = retcode
            self.stdout = stdout_data
            self.stderr = stderr_data

    result = Result(returncode, stdout, stderr)

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
