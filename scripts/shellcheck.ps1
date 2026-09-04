# Run ShellCheck on shell scripts
# ShellCheck is a shell script linter
# Note: Write-Host is intentional for CLI status (PSScriptAnalyzer may flag PSAvoidUsingWriteHost).

# Merge Machine and User PATH so `shellcheck` is found in this session after `winget install`
# without requiring a new terminal (winget updates User PATH).
foreach ($scope in @('Machine', 'User')) {
    $extra = [Environment]::GetEnvironmentVariable('Path', $scope)
    if ($extra) {
        $env:Path = $env:Path + ';' + $extra
    }
}

$shellcheckPath = Get-Command shellcheck -ErrorAction SilentlyContinue

if (-not $shellcheckPath) {
    Write-Host "ERROR: shellcheck not found. Install with:" -ForegroundColor Red
    Write-Host "  Windows (recommended): winget install -e --id koalaman.shellcheck" -ForegroundColor Yellow
    Write-Host "  Or Chocolatey: choco install shellcheck" -ForegroundColor Yellow
    Write-Host "  Or download from: https://github.com/koalaman/shellcheck/releases" -ForegroundColor Yellow
    exit 1
}

Write-Host "Running ShellCheck on shell scripts..." -ForegroundColor Cyan
Write-Host "This will check for shell script quality issues..." -ForegroundColor Gray

# Resolve repo root (Makefile runs from project root; support running the script from elsewhere)
$repoRoot = Split-Path -Parent $PSScriptRoot
$scriptsDir = Join-Path $repoRoot "scripts"

# Find all .sh files in scripts directory
$shFiles = Get-ChildItem -Path $scriptsDir -Filter "*.sh" -Recurse -ErrorAction SilentlyContinue

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
