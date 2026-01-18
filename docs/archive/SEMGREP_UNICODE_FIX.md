# Semgrep Unicode Encoding Fix

## Problem

Running semgrep on Windows systems encountered `UnicodeEncodeError` when semgrep attempted to process or display rules containing Unicode characters (specifically `\u202a` - LEFT-TO-RIGHT EMBEDDING control character). This occurred because Windows' default console encoding (`cp1252`) cannot handle these Unicode characters.

## Solution

### 1. Python Wrapper (`scripts/semgrep.py`)

**Changes:**
- Reconfigured `sys.stdout` and `sys.stderr` to use UTF-8 encoding on Windows
- Set `PYTHONUTF8=1` environment variable for subprocess
- Added explicit UTF-8 encoding to `subprocess.run()` with `errors="replace"`
- Replaced Unicode emoji characters with ASCII equivalents

**Technical Details:**
```python
# Force UTF-8 for the Python interpreter's output streams
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Set environment variable for subprocesses
os.environ["PYTHONUTF8"] = "1"

# Use UTF-8 encoding in subprocess call
result = subprocess.run(
    cmd,
    encoding="utf-8",
    errors="replace",
    ...
)
```

### 2. PowerShell Wrapper (`scripts/semgrep-autofix.ps1`)

**Purpose:** Enables direct semgrep invocation with autofix functionality

**Changes:**
- Created PowerShell script that sets `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8`
- Runs `semgrep scan --config=auto --autofix .` with optional additional arguments
- Accepts additional semgrep arguments (e.g., `--verbose`) passed through to semgrep
- Added `make semgrep-autofix` target to Makefile

## Usage

### Run Security Scan
```bash
make semgrep
```

### Run Security Scan with Auto-fix
```bash
make semgrep-autofix
```

### Direct Semgrep Commands

If you need to run semgrep with custom parameters, set the environment variables first:

**PowerShell:**
```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
semgrep scan --config=auto .
```

**Alternative (using the wrapper):**
```powershell
# Basic usage
.\scripts\semgrep-autofix.ps1

# With additional arguments (e.g., --verbose)
.\scripts\semgrep-autofix.ps1 --verbose

# With output redirection
.\scripts\semgrep-autofix.ps1 --verbose | tee semgrep-output.txt
```

## Root Cause

The issue stems from a mismatch between:
1. **Semgrep rules** downloaded from the registry contain Unicode characters
2. **Windows console encoding** defaults to `cp1252` (Western European)
3. **Python's default behavior** inherits the system's console encoding

The Unicode LEFT-TO-RIGHT EMBEDDING character (`\u202a`) is used in semgrep rules for formatting but cannot be represented in `cp1252` encoding.

## Why This Solution Works

1. **PYTHONUTF8=1**: Forces Python 3.7+ to use UTF-8 mode on all platforms
2. **sys.stdout reconfiguration**: Changes the already-running interpreter's output encoding
3. **subprocess encoding parameter**: Ensures subprocess output is decoded as UTF-8
4. **errors="replace"**: Substitutes undecodable characters with replacement markers instead of crashing

## Testing

Both commands have been tested and verified:
- ✅ `make semgrep` - Successfully scans entire repository
- ✅ `make semgrep-autofix` - Successfully scans and auto-fixes issues
- ✅ No Unicode encoding errors
- ✅ Proper error reporting maintained

## Notes

- The remaining linter warning about catching broad `Exception` is intentional
- The solution is Windows-specific but doesn't break functionality on other platforms
- ASCII text replacements for emojis: ✅→[OK], ❌→[ERROR], ⚠️→[WARNING], 💡→[TIP], 🎉→[SUCCESS]

## References

- [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
- [Windows Console and Unicode](https://docs.python.org/3/using/windows.html#utf-8-mode)
- [Semgrep Documentation](https://semgrep.dev/docs/)
