#!/usr/bin/env python3
"""Run CI test suite with cross-platform CI detection."""

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
    # In CI, use the venv Python explicitly to ensure pytest is available
    # Check for venv Python first (CI uses .venv-ci, local uses .venv)
    # pylint: disable=invalid-name
    # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
    venv_python = None  # noqa: N806
    for venv_name in [".venv-ci", ".venv"]:
        # Handle both Unix and Windows paths
        if sys.platform == "win32":
            venv_path = os.path.join(PROJECT_ROOT, venv_name, "Scripts", "python.exe")
        else:
            venv_path = os.path.join(PROJECT_ROOT, venv_name, "bin", "python")
        # Use absolute path and resolve symlinks to get the actual Python executable
        venv_path = os.path.abspath(venv_path)
        if os.path.exists(venv_path):
            # Resolve symlinks to get the actual Python (venv Python may be symlinked)
            venv_python_real = os.path.realpath(venv_path)
            venv_python = venv_path  # Keep original path for subprocess (works better)
            print(f"[INFO] Found venv Python: {venv_python}")
            print(f"[INFO] Resolved to: {venv_python_real}")
            # Check if pytest is actually installed by checking site-packages
            # Get site-packages for this venv
            # pylint: disable=invalid-name
            # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
            venv_site_packages = None  # noqa: N806
            try:
                # Try to get site-packages by running Python from venv
                result = safe_run_static(
                    venv_python,
                    "-c",
                    "import site; print(site.getsitepackages()[0] if site.getsitepackages() else site.getusersitepackages())",
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0:
                    venv_site_packages = result.stdout.strip()
                    print(f"[INFO] Venv site-packages (from Python): {venv_site_packages}")
                    # Check if this is actually in the venv directory or in the base Python
                    if venv_name not in venv_site_packages:
                        print(
                            "[WARN] Site-packages is NOT in venv directory - this is the base Python's site-packages!"
                        )
                        # Try to find the actual venv site-packages directory
                        venv_lib_dir = os.path.join(PROJECT_ROOT, venv_name, "lib")
                        if os.path.exists(venv_lib_dir):
                            # Find pythonX.Y directory
                            python_dirs = [d for d in os.listdir(venv_lib_dir) if d.startswith("python")]
                            if python_dirs:
                                actual_venv_site_packages = os.path.join(venv_lib_dir, python_dirs[0], "site-packages")
                                print(f"[INFO] Actual venv site-packages should be: {actual_venv_site_packages}")
                                if os.path.exists(actual_venv_site_packages):
                                    venv_site_packages = actual_venv_site_packages
                                    print(f"[INFO] Using actual venv site-packages: {venv_site_packages}")
                    # Check if pytest is in site-packages
                    pytest_path = os.path.join(venv_site_packages, "pytest")
                    if os.path.exists(pytest_path):
                        print(f"[INFO] pytest found in venv site-packages: {pytest_path}")
                    else:
                        print(f"[WARN] pytest NOT found in venv site-packages: {pytest_path}")
                        # List what IS in site-packages for debugging
                        if os.path.exists(venv_site_packages):
                            try:
                                contents = os.listdir(venv_site_packages)
                                print(f"[INFO] Site-packages contents: {contents[:10]}")  # First 10 entries
                            except (OSError, PermissionError):
                                # OSError: file system errors, PermissionError: access denied
                                # Silently ignore - this is just for debugging output
                                pass
            except (OSError, subprocess.SubprocessError, ValueError) as e:
                # OSError: file system errors, subprocess.SubprocessError: subprocess issues,
                # ValueError: invalid arguments to safe_run_static
                print(f"[WARN] Could not check site-packages: {e}")
            # Verify pytest is available in this venv
            try:
                result = safe_run_static(
                    venv_python,
                    "-m",
                    "pytest",
                    "--version",
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0:
                    print("[INFO] Verified pytest is available in venv")
                else:
                    print(f"[WARN] pytest not available in venv: {result.stderr}")
                    print(f"[WARN] Command used: {venv_python} -m pytest --version")
            except (OSError, subprocess.SubprocessError, ValueError) as e:
                # OSError: file system errors, subprocess.SubprocessError: subprocess issues,
                # ValueError: invalid arguments to safe_run_static
                print(f"[WARN] Could not verify pytest in venv: {e}")
            break

    if not venv_python:
        print(f"[WARN] No venv Python found, using sys.executable: {sys.executable}")
        print(f"[WARN] PROJECT_ROOT: {PROJECT_ROOT}")
        # List available venv directories for debugging
        for venv_name in [".venv-ci", ".venv"]:
            venv_dir = os.path.join(PROJECT_ROOT, venv_name)
            if os.path.exists(venv_dir):
                print(f"[INFO] Found venv directory: {venv_dir}")
                bin_dir = os.path.join(venv_dir, "bin" if sys.platform != "win32" else "Scripts")
                if os.path.exists(bin_dir):
                    print(f"[INFO] Found bin directory: {bin_dir}")
                    try:
                        python_files = [f for f in os.listdir(bin_dir) if f.startswith("python")]
                        print(f"[INFO] Python files in bin: {python_files}")
                    except OSError:
                        pass

    # Use venv Python if found, otherwise fall back to sys.executable
    # In CI, when we're invoked as .venv-ci/bin/python, sys.executable is already the venv Python
    # so we should use it directly to avoid symlink resolution issues
    # Normalize paths for comparison (os.path.abspath handles different path formats)
    sys_executable_normalized = os.path.abspath(sys.executable)
    if IN_CI and venv_python and sys_executable_normalized == venv_python:
        # We're already running in the venv Python, use sys.executable directly
        # This ensures we use the exact same Python instance that's running this script
        # pylint: disable=invalid-name
        # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
        python_exe = sys.executable  # noqa: N806
        print(f"[INFO] In CI with venv Python, using sys.executable: {python_exe}")
        print(f"[INFO] sys.executable normalized: {sys_executable_normalized}")
        print(f"[INFO] venv_python: {venv_python}")
    elif venv_python:
        # Use the venv Python we found
        # pylint: disable=invalid-name
        # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
        python_exe = venv_python  # noqa: N806
        print(f"[INFO] Using venv Python: {python_exe}")
    else:
        # Fall back to sys.executable
        # pylint: disable=invalid-name
        # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
        python_exe = sys.executable  # noqa: N806
        print(f"[INFO] No venv found, using sys.executable: {python_exe}")

    # CRITICAL VERIFICATION: Ensure this Python actually has pytest before proceeding
    # This fails fast and prevents wasting CI minutes on failed test runs
    print(f"\n[VERIFICATION] Checking if pytest is available in: {python_exe}")
    print("[VERIFICATION] This is the Python that will be used for: python -m pytest")

    # When venv Python is a symlink, we need to set VIRTUAL_ENV AND PYTHONPATH
    # to ensure it uses the venv's site-packages, not the base Python's
    verify_env = os.environ.copy()
    if IN_CI and venv_python and sys_executable_normalized == venv_python:
        # We're in CI using a symlinked venv Python - need to set VIRTUAL_ENV and PYTHONPATH
        # to ensure it uses the venv's site-packages
        venv_dir = os.path.dirname(os.path.dirname(venv_python))  # Go up from bin/python
        venv_site_packages = os.path.join(venv_dir, "lib", "python3.12", "site-packages")
        verify_env["VIRTUAL_ENV"] = venv_dir
        # PYTHONPATH must include the venv's site-packages for symlinked Python to find packages
        existing_pythonpath = verify_env.get("PYTHONPATH", "")
        if existing_pythonpath:
            verify_env["PYTHONPATH"] = f"{venv_site_packages}:{existing_pythonpath}"
        else:
            verify_env["PYTHONPATH"] = venv_site_packages
        print(f"[VERIFICATION] Setting VIRTUAL_ENV={venv_dir} to ensure venv site-packages are used")
        print(f"[VERIFICATION] Setting PYTHONPATH={venv_site_packages} to ensure packages are found")

    try:
        # First, verify the Python path is what we expect
        python_path_check = safe_run_static(
            python_exe,
            "-c",
            "import sys; print(sys.executable)",
            capture_output=True,
            text=True,
            check=False,
            env=verify_env,
        )
        if python_path_check.returncode == 0:
            actual_python_path = python_path_check.stdout.strip()
            print(f"[VERIFICATION] Python resolves to: {actual_python_path}")
            if actual_python_path != python_exe:
                print(f"[WARNING] Path mismatch - requested: {python_exe}, actual: {actual_python_path}")

        # Now verify pytest is importable
        result = safe_run_static(
            python_exe,
            "-c",
            "import pytest; print(f'pytest {pytest.__version__}')",
            capture_output=True,
            text=True,
            check=False,
            env=verify_env,
        )
        if result.returncode == 0:
            print(f"[VERIFICATION] ✓ pytest IS available: {result.stdout.strip()}")
        else:
            print("[VERIFICATION] ✗ pytest NOT available!")
            print(f"[VERIFICATION] Error: {result.stderr}")
            print(f"[VERIFICATION] Command tried: {python_exe} -c 'import pytest; print(pytest.__version__)'")
            # In CI, this is a fatal error - fail immediately to save CI minutes
            if IN_CI:
                print("\n[FATAL ERROR] Cannot run tests - pytest not found in CI environment")
                print(f"[FATAL ERROR] This Python does not have pytest installed: {python_exe}")
                print("[FATAL ERROR] Check the dependency installation step in the workflow")
                sys.exit(1)
            else:
                print("[WARNING] pytest not available - tests may fail")
    except (OSError, subprocess.SubprocessError, ValueError) as e:
        # OSError: file system errors, subprocess.SubprocessError: subprocess issues,
        # ValueError: invalid arguments to safe_run_static
        print(f"[VERIFICATION] ✗ Error checking pytest: {e}")
        if IN_CI:
            print("[FATAL ERROR] Cannot verify pytest in CI environment")
            sys.exit(1)
        else:
            print("[WARNING] Could not verify pytest - tests may fail")
    # Set environment variables to prevent output buffering issues in CI/Docker
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    # When using a symlinked venv Python, we must set VIRTUAL_ENV and PYTHONPATH to ensure
    # Python uses the venv's site-packages, not the base Python's
    if IN_CI and venv_python and sys_executable_normalized == venv_python:
        venv_dir = os.path.dirname(os.path.dirname(venv_python))  # Go up from bin/python to venv root
        venv_site_packages = os.path.join(venv_dir, "lib", "python3.12", "site-packages")
        env["VIRTUAL_ENV"] = venv_dir
        # PYTHONPATH must include the venv's site-packages for symlinked Python to find packages
        existing_pythonpath = env.get("PYTHONPATH", "")
        if existing_pythonpath:
            env["PYTHONPATH"] = f"{venv_site_packages}:{existing_pythonpath}"
        else:
            env["PYTHONPATH"] = venv_site_packages
        print(f"[INFO] Setting VIRTUAL_ENV={venv_dir} to ensure venv site-packages are used for pytest")
        print(f"[INFO] Setting PYTHONPATH={venv_site_packages} to ensure packages are found")

    # Run tests with coverage
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
    # Non-CI execution path (local development)
    print("Building Docker runner image (this ensures dependencies are up-to-date)...")
    ACT_RUNNER_IMAGE = "mythosmud-gha-runner:latest"
    ACT_RUNNER_DOCKERFILE = "Dockerfile.github-runner"

    # Try building with cache first for speed
    # If cache corruption error occurs, retry with --no-cache
    # Use explicit UTF-8 encoding to handle Docker output on Windows
    try:
        result = safe_run_static(
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
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except subprocess.CalledProcessError as e:
        # Check if error is due to corrupted Docker build cache
        # Error message typically contains "parent snapshot" and "does not exist"
        error_output = ""
        if e.stderr:
            error_output += str(e.stderr)
        if e.stdout:
            error_output += str(e.stdout)
        if hasattr(e, "output") and e.output:
            error_output += str(e.output)

        if "parent snapshot" in error_output and "does not exist" in error_output:
            print("Docker build cache appears corrupted. Retrying with --no-cache...")
            safe_run_static(
                "docker",
                "build",
                "--pull",
                "--no-cache",
                "-t",
                ACT_RUNNER_IMAGE,
                "-f",
                ACT_RUNNER_DOCKERFILE,
                ".",
                cwd=PROJECT_ROOT,
                check=True,
                encoding="utf-8",
                errors="replace",
            )
        else:
            # Re-raise if it's a different error
            raise

    print("Running CI test suite in Docker (coverage enforced)...")
    print("Starting PostgreSQL service in container...")

    # Convert Windows path to Docker-compatible path
    workspace_path = PROJECT_ROOT
    if sys.platform == "win32":
        # Convert Windows path to WSL/Docker format if needed
        # For Docker Desktop on Windows, we can use the path as-is with proper escaping
        workspace_path = PROJECT_ROOT.replace("\\", "/")

    # pylint: disable=invalid-name
    # Variable name follows Python convention (not a constant, so lowercase_with_underscores is correct)
    docker_cmd = (  # noqa: N806
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
        # Playwright E2E tests are excluded from test-ci (run separately in CI workflow)
        # "cd /workspace/client && npm run test && "
        # Use .venv-ci from Docker volume (preserved from build, not overwritten by mount)
        # Ensure pytest-mock and pytest-xdist are installed in the venv before running tests
        # pytest-xdist is required for -n auto in pytest.ini
        "cd /workspace && source .venv-ci/bin/activate && "
        "uv pip install pytest-mock>=3.14.0 pytest-xdist>=3.8.0 && "
        "PYTHONUNBUFFERED=1 pytest server/tests/ --cov=server --cov-report=xml --cov-report=html "
        "--cov-config=.coveragerc -v --tb=short && "
        "python scripts/check_coverage_thresholds.py"
    )

    # Mount workspace from host, but use Docker volumes to override dependencies and caches
    # This ensures we only use source code from the host, not host's .venv, node_modules, or caches
    # Docker volumes take precedence over bind mounts, so host dependencies are ignored
    # This avoids Windows filesystem I/O issues and ensures Linux-specific dependencies work correctly
    # Use Popen with real-time output to avoid deadlock from output buffering
    start_time = time.time()
    # Project requires Python >= 3.12, so encoding/errors arguments are available
    # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen2
    # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen1
    process = subprocess.Popen(
        [
            "docker",
            "run",
            "--rm",
            # Set CI environment variables for proper test behavior (headless mode, etc.)
            "-e",
            "CI=1",
            "-e",
            "GITHUB_ACTIONS=1",
            # Mount workspace (source code only - dependencies overridden by volumes below)
            "-v",
            f"{PROJECT_ROOT}:/workspace",
            # Override host dependencies with Docker volumes (Linux-specific)
            "-v",
            "mythosmud-node-modules:/workspace/client/node_modules",
            "-v",
            "mythosmud-venv-ci:/workspace/.venv-ci",
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
        # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen1
        encoding="utf-8",
        # nosemgrep: python.lang.compatibility.python36.python36-compatibility-Popen2
        errors="replace",
        bufsize=1,  # Line buffered
    )

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

        # pylint: disable=invalid-name
        # Variable names follow Python convention (not constants, so lowercase_with_underscores is correct)
        # These match subprocess.CompletedProcess interface (returncode, stdout, stderr)
        returncode = process.returncode if process.poll() is not None else 1  # noqa: N806
        stdout = "".join(output_lines)  # noqa: N806
        stderr = ""  # noqa: N806
    except (OSError, KeyboardInterrupt, RuntimeError) as e:
        process.kill()
        # pylint: disable=invalid-name
        # Variable names follow Python convention (not constants, so lowercase_with_underscores is correct)
        returncode = 1  # noqa: N806
        stdout = "".join(output_lines)  # noqa: N806
        stderr = str(e)  # noqa: N806

    # Create result-like object
    class Result:
        """Container for subprocess result data (returncode, stdout, stderr)."""

        def __init__(self, retcode, stdout_data, stderr_data):
            # pylint: disable=invalid-name
            # Attribute names match subprocess.CompletedProcess interface (returncode, stdout, stderr)
            # These are instance attributes, not constants, so lowercase_with_underscores is correct
            self.returncode = retcode  # noqa: N806
            self.stdout = stdout_data
            self.stderr = stderr_data

    result = Result(returncode, stdout, stderr)

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
