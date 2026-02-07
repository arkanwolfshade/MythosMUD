import shutil
import subprocess
import sys

from utils.safe_subprocess import safe_run_static

success = True

# Same invocation and args as CI ("Lint with ruff": python -m ruff check --line-length=120 server/)
# so we find the same findings locally. --fix so local auto-fixes when possible.
print("Running ruff linting (python -m ruff, matches CI, with --fix)...")
result = safe_run_static("uv", "run", "python", "-m", "ruff", "check", "--fix", "--line-length=120", "server/", cwd=".")
if result.returncode != 0:
    print(f"Ruff linting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff linting passed!")

# Verify npx is available and get its path for Windows compatibility
# On Windows, subprocess.run needs the full path; on Unix, it can use PATH lookup
npx_path = shutil.which("npx")
if not npx_path:
    msg = "npx not found in PATH. Please install Node.js and ensure npx is available."
    print(msg)
    sys.exit(1)

# ESLint in client
print("Running ESLint in client...")
# Use subprocess.run with validated npx_path from shutil.which()
#
# SAFETY MEASURES FOR SUBPROCESS.RUN WITH NON-STATIC EXECUTABLE:
# 1. npx_path comes from shutil.which("npx") - resolves trusted system executables from PATH
# 2. npx_path is validated to exist before use (checked above with `if not npx_path`)
# 3. All command arguments are static strings ("eslint", "--fix", ".") - no user input
# 4. shell=False is implicit (using list form) - prevents shell injection
# 5. cwd is a static string "client" - no path traversal risk
#
# Why npx_path must be a variable:
# - On Windows, subprocess.run cannot resolve "npx" from PATH automatically
# - We must use shutil.which() to get the full path for Windows compatibility
# - The path is validated to exist and comes from trusted system PATH
#
# This pattern is safe because the executable path is from system PATH (trusted source)
# and all arguments are static strings with no user input or shell interpretation.
# nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
# nosec B603: npx_path is from shutil.which (trusted system PATH), args are static list (not shell=True)
result = subprocess.run([npx_path, "eslint", "--fix", "."], cwd="client", check=False)
if result.returncode != 0:
    print(f"ESLint failed with exit code: {result.returncode}")
    success = False
else:
    print("ESLint passed!")

if not success:
    sys.exit(1)

print("All linting passed!")
