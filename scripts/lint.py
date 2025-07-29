import shutil
import subprocess
import sys

success = True

# Ruff linting in server using uv
print("Running ruff linting in server...")
cmd = ["uv", "run", "--active", "ruff", "check", "server"]
result = subprocess.run(cmd, cwd=".")
if result.returncode != 0:
    print(f"❌ Ruff linting failed with exit code: {result.returncode}")
    success = False
else:
    print("✅ Ruff linting passed!")

# Detect full path to npx
npx_path = shutil.which("npx")
if not npx_path:
    msg = "❌ npx not found in PATH. Please install Node.js and ensure npx is available."
    print(msg)
    sys.exit(1)

# ESLint in client
print("Running ESLint in client...")
npx_cmd = [npx_path, "eslint", "."]
result = subprocess.run(npx_cmd, cwd="client")
if result.returncode != 0:
    print(f"❌ ESLint failed with exit code: {result.returncode}")
    success = False
else:
    print("✅ ESLint passed!")

if not success:
    sys.exit(1)

print("🎉 All linting passed!")
