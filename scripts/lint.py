import subprocess
import sys
import os
import shutil

is_windows = sys.platform.startswith("win")
venv_python = os.path.join("server", "venv", "Scripts" if is_windows else "bin", "python")

success = True

# Ruff linting in server
cmd = [venv_python, "-m", "ruff", "check", "."]
print(f"Running {' '.join(str(c) for c in cmd)} in server...")
result = subprocess.run(cmd, cwd="server")
if result.returncode != 0:
    print(f"Command {' '.join(str(c) for c in cmd)} failed in server")
    success = False

# Detect full path to npx
npx_path = shutil.which("npx")
if not npx_path:
    print("npx not found in PATH. Please install Node.js and ensure npx is available.")
    sys.exit(1)

# ESLint in client
npx_cmd = [npx_path, "eslint", "."]
print(f"Running {' '.join(str(c) for c in npx_cmd)} in client...")
result = subprocess.run(npx_cmd, cwd="client")
if result.returncode != 0:
    print(f"Command {' '.join(str(c) for c in npx_cmd)} failed in client")
    success = False

if not success:
    sys.exit(1)
