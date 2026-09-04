import os
import sys

from utils.safe_subprocess import safe_run_static

main_py = os.path.join("server", "main.py")

print(f"Running server: python {main_py}")
result = safe_run_static("python", main_py)

if result.returncode != 0:
    print(f"Server exited with code: {result.returncode}")
    sys.exit(result.returncode)
