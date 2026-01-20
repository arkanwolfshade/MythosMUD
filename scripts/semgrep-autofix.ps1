# Semgrep Autofix Wrapper for Windows
# This script sets the necessary environment variables to handle Unicode
# characters in semgrep rules on Windows systems.
# Usage: .\scripts\semgrep-autofix.ps1 [additional semgrep arguments]
# Example: .\scripts\semgrep-autofix.ps1 --verbose

# Force UTF-8 encoding to prevent UnicodeEncodeError
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

Write-Host "Running semgrep with autofix..."
Write-Host "This will automatically fix some issues found by semgrep..."
Write-Host ""

# Get additional arguments passed to the script
$additionalArgs = $args

# Build the semgrep command with base arguments
$semgrepArgs = @("scan", "--config=auto", "--autofix", ".")

# Add any additional arguments passed to the script
if ($additionalArgs.Count -gt 0) {
    $semgrepArgs += $additionalArgs
}

# Run semgrep with all arguments
& semgrep $semgrepArgs

$exitCode = $LASTEXITCODE

if ($exitCode -eq 0) {
    Write-Host ""
    Write-Host "[SUCCESS] Semgrep autofix completed successfully!"
}
else {
    Write-Host ""
    Write-Host "[ERROR] Semgrep autofix encountered errors (exit code: $exitCode)"
}

exit $exitCode
