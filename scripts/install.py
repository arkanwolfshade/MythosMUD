import subprocess
import sys
import os

is_windows = sys.platform.startswith("win")
venv_dir = os.path.join("server", "venv")
venv_python = os.path.join(venv_dir, "Scripts" if is_windows else "bin", "python")
venv_pip = os.path.join(venv_dir, "Scripts" if is_windows else "bin", "pip")

steps = [
    [sys.executable, "-m", "venv", venv_dir],
    [venv_pip, "install", "--upgrade", "pip"],
    [venv_pip, "install", "-r", os.path.join("server", "requirements.txt")],
    ["npx", "--version"],  # Ensure npx is available
    ["npm", "install"],
    [sys.executable, "-m", "pip", "install", "pre-commit"],
    ["pre-commit", "install", "-f"],
]

print("Installing server and client dependencies...")

for i, step in enumerate(steps):
    if i == 4:
        # npm install in client
        result = subprocess.run(step, cwd="client")
    else:
        result = subprocess.run(step)
    if result.returncode != 0:
        print(f"Step failed: {' '.join(str(s) for s in step)}")
        sys.exit(result.returncode)
