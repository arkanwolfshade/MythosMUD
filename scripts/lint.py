import shutil
import subprocess
import sys

from utils.safe_subprocess import safe_run_static

success = True

# Ruff linting on entire repository (matching pre-commit hooks)
print("Running ruff linting on entire repository...")
result = safe_run_static("uv", "run", "--active", "ruff", "check", "--fix", "--line-length=120", ".", cwd=".")
if result.returncode != 0:
    print(f"Ruff linting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff linting passed!")

# Verify npx is available and get its path
npx_path = shutil.which("npx")
if not npx_path:
    msg = "npx not found in PATH. Please install Node.js and ensure npx is available."
    print(msg)
    sys.exit(1)

# ESLint in client
print("Running ESLint in client...")
# Use subprocess.run directly for system executables (like format.py does)
# We've already verified npx exists via shutil.which
# nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
# nosec B603: npx_path is from shutil.which (trusted system path), args are list (not shell=True)
result = subprocess.run([npx_path, "eslint", "--fix", "."], cwd="client", check=False)
if result.returncode != 0:
    print(f"ESLint failed with exit code: {result.returncode}")
    success = False
else:
    print("ESLint passed!")

if not success:
    sys.exit(1)

print("All linting passed!")
