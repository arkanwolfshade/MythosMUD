import os
import subprocess
import sys

# Change to server directory and run pytest with coverage
cmd = ["pytest", "--cov=.", "--cov-report=term-missing", "tests"]
env = dict(**os.environ)

print("Running pytest with coverage for world_loader...")
result = subprocess.run(cmd, env=env, cwd="server")
if result.returncode != 0:
    print("Coverage run failed.")
    sys.exit(result.returncode)
