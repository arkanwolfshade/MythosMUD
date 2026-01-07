# Run ShellCheck on shell scripts
# ShellCheck is a shell script linter
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and error messages require Write-Host for proper display')]

$shellcheckPath = Get-Command shellcheck -ErrorAction SilentlyContinue

if (-not $shellcheckPath) {
    Write-Host "ERROR: shellcheck not found. Install with:" -ForegroundColor Red
    Write-Host "  Windows: choco install shellcheck" -ForegroundColor Yellow
    Write-Host "  Or download from: https://github.com/koalaman/shellcheck/releases" -ForegroundColor Yellow
    exit 1
}

Write-Host "Running ShellCheck on shell scripts..." -ForegroundColor Cyan
Write-Host "This will check for shell script quality issues..." -ForegroundColor Gray

# Find all .sh files in scripts directory
$shFiles = Get-ChildItem -Path "scripts" -Filter "*.sh" -Recurse -ErrorAction SilentlyContinue

if ($shFiles.Count -eq 0) {
    Write-Host "[WARNING] No .sh files found in scripts directory" -ForegroundColor Yellow
    exit 0
}

$success = $true
foreach ($file in $shFiles) {
    try {
        & shellcheck $file.FullName
        if ($LASTEXITCODE -ne 0) {
            Write-Host "[WARNING] ShellCheck found issues in $($file.Name)" -ForegroundColor Yellow
            $success = $false
        }
    } catch {
        Write-Host "[ERROR] Error running shellcheck on $($file.Name): $_" -ForegroundColor Red
        $success = $false
    }
}

if (-not $success) {
    exit 1
}

Write-Host ""
Write-Host "[SUCCESS] All ShellCheck checks passed!" -ForegroundColor Green
