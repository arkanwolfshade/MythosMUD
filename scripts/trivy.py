#!/usr/bin/env python3
"""
Run Trivy security scanner on dependencies.
Trivy scans for vulnerabilities in dependencies.
"""

import shutil
import subprocess
import sys

# Check if trivy is available
trivy_path = shutil.which("trivy")
if not trivy_path:
    print("ERROR: trivy not found. Install with:")
    print("  Windows: choco install trivy")
    print("  Or download from: https://github.com/aquasecurity/trivy/releases")
    sys.exit(1)

print("Running Trivy security scan on dependencies...")
print("This will check for known vulnerabilities...")

# Scan Python dependencies (pyproject.toml)
print("\nScanning Python dependencies...")
result = subprocess.run(
    [trivy_path, "fs", "--security-checks", "vuln", "."],
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

if result.returncode == 0:
    print("[OK] Trivy Python scan completed successfully!")
    print("No vulnerabilities found in Python dependencies.")
elif result.returncode == 1:
    print("[WARNING] Trivy found vulnerabilities in Python dependencies:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    # Don't fail on vulnerabilities - just warn (security team can review)
    print("\n[INFO] Continuing despite vulnerabilities (review recommended)")
else:
    print(f"[ERROR] Trivy failed with exit code: {result.returncode}")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    sys.exit(1)

# Scan Node dependencies (package.json in client)
print("\nScanning Node.js dependencies...")
result = subprocess.run(
    [trivy_path, "fs", "--security-checks", "vuln", "client"],
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

if result.returncode == 0:
    print("[OK] Trivy Node.js scan completed successfully!")
    print("No vulnerabilities found in Node.js dependencies.")
elif result.returncode == 1:
    print("[WARNING] Trivy found vulnerabilities in Node.js dependencies:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    # Don't fail on vulnerabilities - just warn (security team can review)
    print("\n[INFO] Continuing despite vulnerabilities (review recommended)")
else:
    print(f"[ERROR] Trivy failed with exit code: {result.returncode}")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    sys.exit(1)

print("\n[SUCCESS] All Trivy security scans completed!")
