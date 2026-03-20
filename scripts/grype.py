#!/usr/bin/env python3
"""
Run Grype vulnerability scanner on the repo root and client (Node) tree.
Primary local/Makefile SCA; see .codacy/codacy.yaml header for Grype vs Trivy (Codacy).
"""

import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

# Check if grype is available in PATH (system installation)
if shutil.which("grype"):
    # Use simple command name for system-installed grype
    # safe_subprocess allows simple command names without path validation
    grype_path = "grype"
else:
    # Fall back to local installation in tools/grype
    project_root = Path(__file__).parent.parent
    local_grype = project_root / "tools" / "grype" / "grype.exe"

    if local_grype.exists():
        grype_path = str(local_grype)
        print(f"Using local Grype installation: {grype_path}")
    else:
        print("ERROR: grype not found. Install with:")
        print("  https://github.com/anchore/grype#installation")
        print("  Windows: choco install grype (or download release asset)")
        sys.exit(1)

print("Running Grype vulnerability scans...")
print("This checks for known CVEs in dependencies on disk.")

print("\nScanning repository root (Python and lockfiles)...")
result = safe_run_static(
    grype_path,
    "dir:.",
    cwd=".",
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

if result.returncode == 0:
    print("[OK] Grype repository root scan completed successfully!")
    print("No vulnerabilities reported for repository root.")
elif result.returncode == 1:
    print("[WARNING] Grype reported vulnerabilities for repository root:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    print("\n[INFO] Continuing despite vulnerabilities (review recommended)")
else:
    print(f"[ERROR] Grype failed for repository root with exit code: {result.returncode}")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    sys.exit(1)

print("\nScanning Node.js tree (client/)...")
result = safe_run_static(
    grype_path,
    "dir:client",
    cwd=".",
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

if result.returncode == 0:
    print("[OK] Grype client scan completed successfully!")
    print("No vulnerabilities reported for client.")
elif result.returncode == 1:
    print("[WARNING] Grype reported vulnerabilities for client:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    print("\n[INFO] Continuing despite vulnerabilities (review recommended)")
else:
    print(f"[ERROR] Grype failed for client with exit code: {result.returncode}")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    sys.exit(1)

print("\n[SUCCESS] All Grype vulnerability scans completed!")
