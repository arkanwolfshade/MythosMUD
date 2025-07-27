import subprocess
import sys

print("Running tests with pytest...")
cmd = ["uv", "run", "pytest", "server/tests", "-v", "--tb=short"]
result = subprocess.run(cmd)

if result.returncode != 0:
    print(f"Tests failed with exit code: {result.returncode}")
    sys.exit(result.returncode)
else:
    print("✅ All tests passed!")
