#!/usr/bin/env python3
"""
Run Grype vulnerability scanner on the repo root and client (Node) tree.
Primary local/Makefile SCA; see .codacy/codacy.yaml header for Grype vs Trivy (Codacy).
"""

import os
import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static


def merge_windows_machine_user_path_into_environ() -> None:
    """Append Machine and User Path from the registry (matches hadolint.ps1 behavior).

    winget/choco installs often update the stored Path before the current process
    inherits it; refreshing avoids false 'grype not found' in the same session.
    """
    if os.name != "nt":
        return
    try:
        import winreg
    except ImportError:
        return
    chunks: list[str] = []
    for root, subkey in (
        (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
        (winreg.HKEY_CURRENT_USER, r"Environment"),
    ):
        try:
            with winreg.OpenKey(root, subkey) as key:
                path_val, _ = winreg.QueryValueEx(key, "Path")
                if isinstance(path_val, str) and path_val.strip():
                    chunks.append(path_val)
        except OSError:
            continue
    if not chunks:
        return
    extra = ";".join(chunks)
    current = os.environ.get("PATH", "")
    os.environ["PATH"] = f"{current};{extra}" if current else extra


def _resolve_grype_executable() -> str | None:
    merge_windows_machine_user_path_into_environ()
    if shutil.which("grype"):
        return "grype"
    project_root = Path(__file__).parent.parent
    local_grype = project_root / "tools" / "grype" / "grype.exe"
    if local_grype.exists():
        return str(local_grype)
    return None


def main() -> int:
    grype_path = _resolve_grype_executable()
    if not grype_path:
        print("ERROR: grype not found. Install with:")
        print("  https://github.com/anchore/grype#installation")
        print("  Windows: winget install -e --id Anchore.Grype")
        print("  Windows: choco install grype (or download release asset)")
        return 1

    if grype_path != "grype":
        print(f"Using local Grype installation: {grype_path}")

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
        return 1

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
        return 1

    print("\n[SUCCESS] All Grype vulnerability scans completed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
