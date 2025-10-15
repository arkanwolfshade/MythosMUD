import shutil
import subprocess
import sys
import os

success = True

# Ruff linting on entire repository (matching pre-commit hooks)
print("Running ruff linting on entire repository...")
# Try to find ruff in common locations
ruff_cmd = None
if shutil.which("ruff"):
    ruff_cmd = "ruff"
elif os.path.exists(os.path.expanduser("~/.local/bin/ruff")):
    ruff_cmd = os.path.expanduser("~/.local/bin/ruff")
else:
    # Try using uv if available
    if shutil.which("uv"):
        cmd = ["uv", "run", "--active", "ruff", "check", "--fix", "--line-length=120", "."]
    else:
        print("Warning: Ruff not found. Trying to install...")
        subprocess.run(["pip3", "install", "ruff==0.12.5"], capture_output=True)
        ruff_cmd = os.path.expanduser("~/.local/bin/ruff")

if ruff_cmd:
    cmd = [ruff_cmd, "check", "--fix", "--line-length=120", "."]
    
result = subprocess.run(cmd, cwd=".")
if result.returncode != 0:
    print(f"Ruff linting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff linting passed!")

# Detect full path to npx
npx_path = shutil.which("npx")
if not npx_path:
    msg = "npx not found in PATH. Please install Node.js and ensure npx is available."
    print(msg)
    sys.exit(1)

# ESLint in client
print("Running ESLint in client...")
npx_cmd = [npx_path, "eslint", "--fix", "."]
client_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "client")
result = subprocess.run(npx_cmd, cwd=client_path)
if result.returncode != 0:
    print(f"ESLint failed with exit code: {result.returncode}")
    success = False
else:
    print("ESLint passed!")

if not success:
    sys.exit(1)

print("All linting passed!")
