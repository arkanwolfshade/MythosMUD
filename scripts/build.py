import subprocess
import sys

cmd = ["npm", "run", "build"]

print("Running npm run build in client directory...")
result = subprocess.run(cmd, cwd="client")
if result.returncode != 0:
    print("Build failed.")
    sys.exit(result.returncode)
