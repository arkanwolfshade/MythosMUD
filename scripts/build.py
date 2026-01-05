import sys

from utils.safe_subprocess import safe_run_static

print("Running npm run build in client directory...")
result = safe_run_static("npm.cmd", "run", "build", cwd="client")
if result.returncode != 0:
    print("Build failed.")
    sys.exit(result.returncode)
