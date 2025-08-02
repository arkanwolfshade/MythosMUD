import os
import subprocess
import sys

print("🧹 Cleaning test database...")
clean_cmd = ["python", "scripts/clean_test_db.py"]

# Set the required environment variables for the subprocess
env = os.environ.copy()
env["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
env["MYTHOS_PERSIST_LOG"] = "server/tests/logs/test_persistence.log"
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
