import os
import subprocess
import sys

is_windows = sys.platform.startswith("win")

# Check if uv is available
try:
    subprocess.run(["uv", "--version"], check=True, capture_output=True)
    print("[OK] uv is available")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("[ERROR] uv is not available. Please install uv first:")
    print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
    print("  # or on Windows:")
    print('  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"')
    sys.exit(1)


def get_project_root():
    """Determine the project root based on current working directory"""
    current_dir = os.getcwd()

    # Check if we're in a worktree
    if "MythosMUD-server" in current_dir:
        # We're in the server worktree, need to go up to main project
        return os.path.dirname(current_dir)
    elif "MythosMUD-client" in current_dir:
        # We're in the client worktree, need to go up to main project
        return os.path.dirname(current_dir)
    elif "MythosMUD-docs" in current_dir:
        # We're in the docs worktree, need to go up to main project
        return os.path.dirname(current_dir)
    elif "MythosMUD-testing" in current_dir:
        # We're in the testing worktree, need to go up to main project
        return os.path.dirname(current_dir)
    else:
        # We're in the main project directory
        return current_dir


project_root = get_project_root()
print(f"Project root: {project_root}")

# Determine if we're in a worktree context
is_worktree = project_root != os.getcwd()
if is_worktree:
    print(f"Worktree context detected: {os.path.basename(os.getcwd())}")

steps = [
    # Install Python dependencies including dev prerequisites
    # --all-extras: includes all optional dependencies from [project.optional-dependencies]
    # --dev: explicitly includes dev dependency group (included by default, but being explicit)
    ["uv", "sync", "--project", "server", "--all-extras", "--dev"],
    ["uv", "run", "--active", "pre-commit", "install", "-f"],
    ["npx.cmd" if is_windows else "npx", "--version"],
    # Install Node dependencies including devDependencies
    # npm install includes devDependencies by default (unless --production is used)
    ["npm.cmd" if is_windows else "npm", "install"],
]

print("PYTHON ENV PATH:", os.environ["PATH"])
print("Installing server and client dependencies...")

for i, step in enumerate(steps):
    print(f"Running: {' '.join(step)}")

    if i == 3:  # npm install in client
        # Always run npm install from the main project's client directory
        client_path = os.path.join(project_root, "client")
        result = subprocess.run(step, cwd=client_path, check=False)
    else:
        # For other steps, run from the project root
        result = subprocess.run(step, cwd=project_root, check=False)

    if result.returncode != 0:
        print(f"[ERROR] Step failed: {' '.join(str(s) for s in step)}")
        sys.exit(result.returncode)
    else:
        print(f"[OK] Step completed: {' '.join(str(s) for s in step)}")

print("[SUCCESS] Installation completed successfully!")
print("\nNext steps:")
print("1. Start the server: scripts/start_server.ps1")
print("2. Start the client: cd client && npm start")

if is_worktree:
    worktree_name = os.path.basename(os.getcwd())
    print(f"\nNote: You're currently in the {worktree_name} worktree.")
    print("   Consider switching to the main worktree for integration tasks.")
