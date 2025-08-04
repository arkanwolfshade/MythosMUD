import os
import subprocess
import sys
from pathlib import Path

print("🧹 Cleaning test database...")
clean_cmd = ["python", "scripts/clean_test_db.py"]

# Set the required environment variables for the subprocess
env = os.environ.copy()
env["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
# Get the project root (one level up from scripts directory)
project_root = Path(__file__).parent.parent
# Ensure we're using the correct path for test logs
test_logs_dir = project_root / "server" / "tests" / "logs"
test_logs_dir.mkdir(parents=True, exist_ok=True)
env["PERSIST_LOG"] = str(test_logs_dir / "test_persistence.log")
env["SERVER_LOG"] = str(test_logs_dir / "test_server.log")
env["ALIASES_DIR"] = "server/tests/data/players/aliases"

clean_result = subprocess.run(clean_cmd, env=env)

if clean_result.returncode != 0:
    print("⚠️  Warning: Failed to clean test database, continuing anyway...")

print("Running tests with pytest...")
cmd = ["uv", "run", "pytest", "server/tests", "-v", "--tb=short"]
result = subprocess.run(cmd, env=env)

if result.returncode != 0:
    print(f"Tests failed with exit code: {result.returncode}")
    sys.exit(result.returncode)
else:
    print("✅ All tests passed!")
