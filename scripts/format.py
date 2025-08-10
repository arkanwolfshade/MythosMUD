import shutil
import subprocess
import sys

success = True

# Ruff formatting in server using uv
print("Running ruff formatting in server...")
cmd = ["uv", "run", "--active", "ruff", "format", "server"]
result = subprocess.run(cmd, cwd=".")
if result.returncode != 0:
    print(f"Ruff formatting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff formatting completed!")

# Detect full path to npm
npm_path = shutil.which("npm")
if not npm_path:
    msg = "npm not found in PATH. Please install Node.js and ensure npm is available."
    print(msg)
    sys.exit(1)

# Prettier formatting in client via npm script
print("Running prettier formatting in client...")
npm_cmd = [npm_path, "run", "format"]
result = subprocess.run(npm_cmd, cwd="client")
if result.returncode != 0:
    print(f"Prettier formatting failed with exit code: {result.returncode}")
    success = False
else:
    print("Prettier formatting completed!")

if not success:
    sys.exit(1)

print("All formatting completed!")
