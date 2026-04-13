import os
import shutil
import subprocess
import sys

from utils.safe_subprocess import safe_run_static

success = True

# Ruff formatting in server using uv (static arguments via safe subprocess wrapper)
print("Running ruff formatting in server...")
result = safe_run_static(
    "uv",
    "run",
    "--active",
    "ruff",
    "format",
    "server",
    cwd=".",
    check=False,
)
if result.returncode != 0:
    print(f"Ruff formatting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff formatting completed!")

# Detect full path to npm
npm_path = shutil.which("npm")
if not npm_path:
    msg = "npm not found in PATH. Please install Node.js and ensure npm is available."
    print(msg)
    sys.exit(1)

# Prettier formatting in client via npm script
print("Running prettier formatting in client...")
_client_nm = os.path.join("client", "node_modules", "prettier")
if not os.path.isdir(_client_nm):
    print(
        f"client/node_modules is missing or Prettier is not installed (expected {_client_nm}).\n"
        + "From this repository root run: make install\n"
        + "(Linked worktrees do not share node_modules; install per checkout.)"
    )
    sys.exit(1)

# On Windows subprocess.run cannot resolve "npm" from PATH; must use full path from shutil.which.
# Executable and args are from trusted PATH / static strings; shell=False; no user input.
# nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
# nosec B603: npm_path from shutil.which (trusted PATH), args are static list
result = subprocess.run(
    [npm_path, "run", "format"],
    cwd="client",
    check=False,
)
if result.returncode != 0:
    print(f"Prettier formatting failed with exit code: {result.returncode}")
    success = False
else:
    print("Prettier formatting completed!")

if not success:
    sys.exit(1)

print("All formatting completed!")
