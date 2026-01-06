# Run Hadolint on Dockerfile
# Hadolint is a Dockerfile linter that checks for best practices
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and error messages require Write-Host for proper display')]

$hadolintPath = Get-Command hadolint -ErrorAction SilentlyContinue

if (-not $hadolintPath) {
    Write-Host "ERROR: hadolint not found. Install with:" -ForegroundColor Red
    Write-Host "  Windows: choco install hadolint" -ForegroundColor Yellow
    Write-Host "  Or download from: https://github.com/hadolint/hadolint/releases" -ForegroundColor Yellow
    exit 1
}

Write-Host "Running Hadolint on Dockerfile..." -ForegroundColor Cyan
Write-Host "This will check for Dockerfile best practices..." -ForegroundColor Gray

$dockerfile = "Dockerfile.github-runner"
if (-not (Test-Path $dockerfile)) {
    Write-Host "[WARNING] Dockerfile not found: $dockerfile" -ForegroundColor Yellow
    exit 0
}

try {
    & hadolint $dockerfile
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Hadolint scan completed successfully!" -ForegroundColor Green
        Write-Host "No Dockerfile issues found." -ForegroundColor Gray
    } else {
        Write-Host "[WARNING] Hadolint found Dockerfile issues" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "[ERROR] Error running hadolint: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[SUCCESS] All Hadolint checks passed!" -ForegroundColor Green
