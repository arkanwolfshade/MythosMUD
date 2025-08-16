import shutil
import subprocess
import sys

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
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")

    if result.returncode == 0:
        print("✅ Semgrep scan completed successfully!")
        print("No security issues or best practice violations found.")
    elif result.returncode == 1:
        print("⚠️  Semgrep found potential issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        success = False
    else:
        print(f"❌ Semgrep failed with exit code: {result.returncode}")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
        success = False

except Exception as e:
    print(f"❌ Error running semgrep: {e}")
    success = False

if not success:
    print("\n💡 To fix issues found by semgrep:")
    print("   - Review the output above for specific issues")
    print("   - Run 'semgrep scan --config=auto --autofix .' to auto-fix some issues")
    print("   - Check semgrep documentation for rule explanations")
    sys.exit(1)

print("\n🎉 All semgrep checks passed!")
print("Your code follows security best practices and coding standards.")
