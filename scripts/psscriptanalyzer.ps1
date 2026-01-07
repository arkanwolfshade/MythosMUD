# Run PSScriptAnalyzer on PowerShell scripts
# PSScriptAnalyzer is the official PowerShell linter

if (-not (Get-Module -ListAvailable -Name PSScriptAnalyzer)) {
    Write-Host "Installing PSScriptAnalyzer module..." -ForegroundColor Cyan
    Install-Module -Name PSScriptAnalyzer -Scope CurrentUser -Force -AllowClobber
}

Write-Host "Running PSScriptAnalyzer on PowerShell scripts..." -ForegroundColor Cyan
Write-Host "This will check for PowerShell best practices..." -ForegroundColor Gray

# Find all .ps1 files in scripts directory
$ps1Files = Get-ChildItem -Path "scripts" -Filter "*.ps1" -Recurse -ErrorAction SilentlyContinue

if ($ps1Files.Count -eq 0) {
    Write-Host "[WARNING] No .ps1 files found in scripts directory" -ForegroundColor Yellow
    exit 0
}

$success = $true
foreach ($file in $ps1Files) {
    try {
        # Exclude PSAvoidUsingWriteHost - Write-Host is appropriate for user-facing status messages
        $results = Invoke-ScriptAnalyzer -Path $file.FullName -Severity Error, Warning -ExcludeRule PSAvoidUsingWriteHost
        if ($results.Count -gt 0) {
            Write-Host "[WARNING] PSScriptAnalyzer found issues in $($file.Name):" -ForegroundColor Yellow
            $results | Format-Table -AutoSize
            $success = $false
        }
    }
    catch {
        Write-Host "[ERROR] Error running PSScriptAnalyzer on $($file.Name): $_" -ForegroundColor Red
        $success = $false
    }
}

if (-not $success) {
    exit 1
}

Write-Host ""
Write-Host "[SUCCESS] All PSScriptAnalyzer checks passed!" -ForegroundColor Green
