import io
import os
import shutil
import subprocess
import sys

# Force UTF-8 encoding to handle Unicode characters in semgrep rules
# This prevents UnicodeEncodeError on Windows when semgrep downloads rules
# containing Unicode control characters (e.g., \u202a)
os.environ["PYTHONUTF8"] = "1"

# Reconfigure stdout and stderr to use UTF-8 encoding
# This is necessary on Windows where the default console encoding is cp1252
# which cannot handle Unicode characters in semgrep rules
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

success = True

# Check if semgrep is available
semgrep_path = shutil.which("semgrep")
if not semgrep_path:
    msg = "semgrep not found in PATH. Please install semgrep: pip install semgrep"
    print(msg)
    sys.exit(1)

print("Running semgrep static analysis on entire repository...")
print("This will check for security vulnerabilities and best practices...")

# Run semgrep with default rules (security and best practices)
# Using --config=auto to automatically detect and use appropriate rules
cmd = [semgrep_path, "scan", "--config=auto", "--json", "--quiet", "."]

try:
    # Use UTF-8 encoding for subprocess to handle Unicode in semgrep output
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=".",
        encoding="utf-8",
        errors="replace",  # Replace undecodable characters instead of failing
        check=False,  # We handle return codes manually
    )

    if result.returncode == 0:
        print("[OK] Semgrep scan completed successfully!")
        print("No security issues or best practice violations found.")
    elif result.returncode == 1:
        print("[WARNING] Semgrep found potential issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        success = False
    else:
        print(f"[ERROR] Semgrep failed with exit code: {result.returncode}")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
        success = False

except Exception as e:  # noqa: BLE001
    # We catch all exceptions here to ensure graceful failure reporting
    print(f"[ERROR] Error running semgrep: {e}")
    success = False

if not success:
    print("\n[TIP] To fix issues found by semgrep:")
    print("   - Review the output above for specific issues")
    print("   - Run 'semgrep scan --config=auto --autofix .' to auto-fix some issues")
    print("   - Check semgrep documentation for rule explanations")
    sys.exit(1)

print("\n[SUCCESS] All semgrep checks passed!")
print("Your code follows security best practices and coding standards.")
