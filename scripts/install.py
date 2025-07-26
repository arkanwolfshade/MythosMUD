import subprocess
import sys

is_windows = sys.platform.startswith("win")

# Check if uv is available
try:
    subprocess.run(["uv", "--version"], check=True, capture_output=True)
    print("✓ uv is available")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("❌ uv is not available. Please install uv first:")
    print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
    print("  # or on Windows:")
    print("  powershell -c \"irm https://astral.sh/uv/install.ps1 | iex\"")
    sys.exit(1)

steps = [
    # Install Python dependencies using uv
    ["uv", "sync", "--project", "server"],
    # Install pre-commit hooks
    ["uv", "run", "--active", "pre-commit", "install", "-f"],
    # Ensure npx is available
    ["npx", "--version"],
    # Install client dependencies
    ["npm", "install"],
]

print("Installing server and client dependencies...")

for i, step in enumerate(steps):
    print(f"Running: {' '.join(step)}")

    if i == 3:  # npm install in client
        result = subprocess.run(step, cwd="client")
    else:
        result = subprocess.run(step)

    if result.returncode != 0:
        print(f"❌ Step failed: {' '.join(str(s) for s in step)}")
        sys.exit(result.returncode)
    else:
        print(f"✓ Step completed: {' '.join(str(s) for s in step)}")

print("✅ Installation completed successfully!")
print("\nNext steps:")
print("1. Start the server: uv run --active uvicorn main:app --reload")
print("2. Start the client: cd client && npm start")
