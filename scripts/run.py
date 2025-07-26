import subprocess
import sys
import os

main_py = os.path.join("server", "main.py")

print(f"Running server: uv run --project server {main_py}")
result = subprocess.run(["uv", "run", "--project", "server", main_py])

if result.returncode != 0:
    print(f"Server exited with code: {result.returncode}")
    sys.exit(result.returncode)
