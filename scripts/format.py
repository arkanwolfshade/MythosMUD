import subprocess
import sys
import os
import shutil

is_windows = sys.platform.startswith("win")
venv_python = os.path.join("server", "venv", "Scripts" if is_windows else "bin", "python")

success = True

# Ruff formatting in server
cmd = [venv_python, "-m", "ruff", "format", "."]
print(f"Running {' '.join(str(c) for c in cmd)} in server...")
result = subprocess.run(cmd, cwd="server")
if result.returncode != 0:
    print(f"Command {' '.join(str(c) for c in cmd)} failed in server")
    success = False

# Detect full path to npm
npm_path = shutil.which("npm")
if not npm_path:
    print("npm not found in PATH. Please install Node.js and ensure npm is available.")
    sys.exit(1)

# Prettier formatting in client via npm script
npm_cmd = [npm_path, "run", "format"]
print(f"Running {' '.join(str(c) for c in npm_cmd)} in client...")
result = subprocess.run(npm_cmd, cwd="client")
if result.returncode != 0:
    print(f"Command {' '.join(str(c) for c in npm_cmd)} failed in client")
    success = False

if not success:
    sys.exit(1)
