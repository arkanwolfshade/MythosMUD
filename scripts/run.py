import subprocess
import sys
import os

is_windows = sys.platform.startswith("win")
venv_python = os.path.join("server", "venv", "Scripts" if is_windows else "bin", "python")
main_py = os.path.join("server", "main.py")

print(f"Running server: {venv_python} {main_py}")
result = subprocess.run([venv_python, main_py])
if result.returncode != 0:
    print("Server exited with error.")
    sys.exit(result.returncode)
