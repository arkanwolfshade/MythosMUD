import subprocess
import sys
import os

cmd = [
    "pytest",
    "--cov=world_loader",
    "--cov-report=term-missing",
    "server/tests"
]
env = dict(**os.environ, PYTHONPATH="server")

print("Running pytest with coverage for world_loader...")
result = subprocess.run(cmd, env=env)
if result.returncode != 0:
    print("Coverage run failed.")
    sys.exit(result.returncode)
