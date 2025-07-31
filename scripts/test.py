import subprocess
import sys

print("🧹 Cleaning test database...")
clean_cmd = ["python", "scripts/clean_test_db.py"]
clean_result = subprocess.run(clean_cmd)

if clean_result.returncode != 0:
    print("⚠️  Warning: Failed to clean test database, continuing anyway...")

print("Running tests with pytest...")
cmd = ["uv", "run", "pytest", "server/tests", "-v", "--tb=short"]
result = subprocess.run(cmd)

if result.returncode != 0:
    print(f"Tests failed with exit code: {result.returncode}")
    sys.exit(result.returncode)
else:
    print("✅ All tests passed!")
