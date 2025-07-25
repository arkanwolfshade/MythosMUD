import subprocess
import sys
import os

is_windows = sys.platform.startswith("win")
venv_python = os.path.join("server", "venv", "Scripts" if is_windows else "bin", "python")

cmd = [venv_python, "-m", "pytest", "server/tests"]

print("Running pytest for server tests...")
result = subprocess.run(cmd)
if result.returncode != 0:
    print("Tests failed.")
    sys.exit(result.returncode)
