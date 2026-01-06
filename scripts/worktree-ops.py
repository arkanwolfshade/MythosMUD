#!/usr/bin/env python3
"""
Worktree-aware operations script for MythosMUD
Handles common tasks across different worktree contexts
"""

import argparse
import os
import subprocess
import sys


def get_project_root():
    """Determine the project root based on current working directory"""
    current_dir = os.getcwd()

    # Check if we're in a worktree
    worktree_indicators = ["MythosMUD-server", "MythosMUD-client", "MythosMUD-docs", "MythosMUD-testing"]

    for indicator in worktree_indicators:
        if indicator in current_dir:
            return os.path.dirname(current_dir)

    # We're in the main project directory
    return current_dir


def get_current_worktree():
    """Get the current worktree name"""
    current_dir = os.getcwd()
    if "MythosMUD-server" in current_dir:
        return "server"
    elif "MythosMUD-client" in current_dir:
        return "client"
    elif "MythosMUD-docs" in current_dir:
        return "docs"
    elif "MythosMUD-testing" in current_dir:
        return "testing"
    else:
        return "main"


def run_command(cmd, cwd=None, check=True):
    """Run a command with proper error handling"""
    if cwd is None:
        cwd = get_project_root()

    print(f"Running: {' '.join(cmd)} (from {os.path.basename(cwd)})")

    try:
        # pylint: disable=import-outside-toplevel
        # Lazy import to avoid circular dependencies and improve startup performance
        from utils.safe_subprocess import safe_run

        result = safe_run(cmd, cwd=cwd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        if check:
            sys.exit(e.returncode)
        return e


def install_dependencies():
    """Install dependencies (worktree-aware)"""
    project_root = get_project_root()
    current_worktree = get_current_worktree()

    print(f"Installing dependencies from {current_worktree} worktree...")

    # Run the install script from project root
    # pylint: disable=import-outside-toplevel
    # Lazy import to avoid circular dependencies and improve startup performance
    from utils.safe_subprocess import safe_run_static

    install_script = os.path.join(project_root, "scripts", "install.py")
    result = safe_run_static(sys.executable, install_script, cwd=project_root, check=False)

    if result.returncode == 0:
        print("[OK] Dependencies installed successfully!")
    else:
        print("[ERROR] Installation failed!")
        sys.exit(result.returncode)


def run_tests():
    """Run tests (worktree-aware)"""
    project_root = get_project_root()
    current_worktree = get_current_worktree()

    print(f"Running tests from {current_worktree} worktree...")

    # pylint: disable=import-outside-toplevel
    from utils.safe_subprocess import safe_run_static

    if current_worktree == "client":
        # Run client tests
        client_path = os.path.join(project_root, "client")
        result = safe_run_static("npm", "test", cwd=client_path, check=False)
    elif current_worktree == "server":
        # Run server tests
        result = safe_run_static("python", "-m", "pytest", cwd=project_root, check=False)
    else:
        # Run all tests
        test_script = os.path.join(project_root, "scripts", "test.py")
        result = safe_run_static(sys.executable, test_script, cwd=project_root, check=False)

    if result.returncode == 0:
        print("[OK] Tests completed successfully!")
    else:
        print("[ERROR] Tests failed!")
        sys.exit(result.returncode)


def run_lint():
    """Run linting (worktree-aware)"""
    project_root = get_project_root()
    current_worktree = get_current_worktree()

    print(f"Running lint from {current_worktree} worktree...")

    from utils.safe_subprocess import safe_run_static

    if current_worktree == "client":
        # Run client lint
        client_path = os.path.join(project_root, "client")
        result = safe_run_static("npm", "run", "lint", cwd=client_path, check=False)
    elif current_worktree == "server":
        # Run server lint
        result = safe_run_static("ruff", "check", "server", cwd=project_root, check=False)
    else:
        # Run all lint
        lint_script = os.path.join(project_root, "scripts", "lint.py")
        result = safe_run_static(sys.executable, lint_script, cwd=project_root, check=False)

    if result.returncode == 0:
        print("[OK] Lint completed successfully!")
    else:
        print("[ERROR] Lint failed!")
        sys.exit(result.returncode)


def run_format():
    """Run formatting (worktree-aware)"""
    project_root = get_project_root()
    current_worktree = get_current_worktree()

    print(f"Running format from {current_worktree} worktree...")

    from utils.safe_subprocess import safe_run_static

    if current_worktree == "client":
        # Run client format
        client_path = os.path.join(project_root, "client")
        result = safe_run_static("npm", "run", "format", cwd=client_path, check=False)
    elif current_worktree == "server":
        # Run server format
        result = safe_run_static("ruff", "format", "server", cwd=project_root, check=False)
    else:
        # Run all format
        format_script = os.path.join(project_root, "scripts", "format.py")
        result = safe_run_static(sys.executable, format_script, cwd=project_root, check=False)

    if result.returncode == 0:
        print("[OK] Format completed successfully!")
    else:
        print("[ERROR] Format failed!")
        sys.exit(result.returncode)


def show_status():
    """Show worktree and project status"""
    project_root = get_project_root()
    current_worktree = get_current_worktree()
    current_dir = os.getcwd()

    print("Worktree Status:")
    print(f"   Current worktree: {current_worktree}")
    print(f"   Current directory: {current_dir}")
    print(f"   Project root: {project_root}")

    # Show git status
    from utils.safe_subprocess import safe_run_static

    print("\nGit Status:")
    result = safe_run_static("git", "status", "--short", cwd=current_dir, capture_output=True, text=True, check=False)
    if result.stdout.strip():
        print(result.stdout)
    else:
        print("   Working directory clean")

    # Show branch info
    result = safe_run_static(
        ["git", "branch", "--show-current"], cwd=current_dir, capture_output=True, text=True, check=False
    )
    if result.returncode == 0:
        branch = result.stdout.strip()
        print(f"   Current branch: {branch}")


def main():
    parser = argparse.ArgumentParser(description="Worktree-aware operations for MythosMUD")
    parser.add_argument("command", choices=["install", "test", "lint", "format", "status"], help="Command to run")

    args = parser.parse_args()

    if args.command == "install":
        install_dependencies()
    elif args.command == "test":
        run_tests()
    elif args.command == "lint":
        run_lint()
    elif args.command == "format":
        run_format()
    elif args.command == "status":
        show_status()


if __name__ == "__main__":
    main()
