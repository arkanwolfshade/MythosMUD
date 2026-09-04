#!/usr/bin/env python3
"""
Run Grype vulnerability scanner from the MythosMUD project root.

Scans Python/uv lockfiles at the repo root and the client/ Node tree. Paths under
e2e-tests/, Playwright harness output, and test-only trees are excluded via .grype.yaml.

Invoke with ``make grype`` from the project root (not bundled in ``make all`` / codacy-tools).
Codacy CI uses Trivy; see .codacy/README.md.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

REPO_ROOT = Path(__file__).resolve().parents[1]
GRYPE_CONFIG = REPO_ROOT / ".grype.yaml"


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


def repo_root() -> Path:
    """Return the MythosMUD project root (parent of scripts/)."""
    return REPO_ROOT


def _resolve_grype_executable() -> str | None:
    merge_windows_machine_user_path_into_environ()
    if shutil.which("grype"):
        return "grype"
    local_grype = REPO_ROOT / "tools" / "grype" / "grype.exe"
    if local_grype.exists():
        return str(local_grype)
    return None


def _grype_command(grype_path: str, target: str) -> list[str]:
    cmd = [grype_path, target]
    if GRYPE_CONFIG.is_file():
        cmd.extend(["--config", str(GRYPE_CONFIG)])
    return cmd


def _run_grype_scan(grype_path: str, target: str, label: str) -> subprocess.CompletedProcess[str]:
    return safe_run_static(
        *_grype_command(grype_path, target),
        cwd=str(REPO_ROOT),
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _handle_grype_result(result: subprocess.CompletedProcess[str], label: str) -> int | None:
    if result.returncode == 0:
        print(f"[OK] Grype {label} scan completed successfully!")
        print(f"No vulnerabilities reported for {label}.")
        return None
    if result.returncode == 1:
        print(f"[WARNING] Grype reported vulnerabilities for {label}:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        print("\n[INFO] Continuing despite vulnerabilities (review recommended)")
        return None
    print(f"[ERROR] Grype failed for {label} with exit code: {result.returncode}")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    return 1


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

    print(f"Running Grype vulnerability scans from project root: {REPO_ROOT}")
    print("This checks for known CVEs in dependencies on disk.")
    if GRYPE_CONFIG.is_file():
        print(f"Using config: {GRYPE_CONFIG}")

    print("\nScanning repository root (Python and lockfiles)...")
    root_result = _run_grype_scan(grype_path, "dir:.", "repository root")
    if (err := _handle_grype_result(root_result, "repository root")) is not None:
        return err

    print("\nScanning Node.js tree (client/)...")
    client_result = _run_grype_scan(grype_path, "dir:client", "client")
    if (err := _handle_grype_result(client_result, "client")) is not None:
        return err

    print("\n[SUCCESS] All Grype vulnerability scans completed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
