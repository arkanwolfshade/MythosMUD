import shutil
import subprocess
import sys

success = True

# Ruff linting on entire repository (matching pre-commit hooks)
print("Running ruff linting on entire repository...")
cmd = [
    "uv", "run", "--active", "ruff", "check", "--fix", "--line-length=120", "."
]
result = subprocess.run(cmd, cwd=".")
if result.returncode != 0:
    print(f"Ruff linting failed with exit code: {result.returncode}")
    success = False
else:
    print("Ruff linting passed!")

# Detect full path to npx
npx_path = shutil.which("npx")
if not npx_path:
    msg = (
        "npx not found in PATH. Please install Node.js and ensure npx is available."
    )
    print(msg)
    sys.exit(1)

# ESLint in client
print("Running ESLint in client...")
npx_cmd = [npx_path, "eslint", "--fix", "."]
result = subprocess.run(npx_cmd, cwd="client")
if result.returncode != 0:
    print(f"ESLint failed with exit code: {result.returncode}")
    success = False
else:
    print("ESLint passed!")

if not success:
    sys.exit(1)

print("All linting passed!")
