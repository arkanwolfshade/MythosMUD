# Run PSScriptAnalyzer on PowerShell scripts
# PSScriptAnalyzer is the official PowerShell linter
# Note: Write-Host is intentional for CLI status (PSScriptAnalyzer may flag PSAvoidUsingWriteHost).

# Windows PowerShell 5.1 often ships with a broken or unloadable PowerShellGet, which breaks
# Install-Module. When pwsh (PowerShell 7+) is installed, re-invoke there for reliable gallery access.
if ($PSVersionTable.PSVersion.Major -lt 7) {
    $pwshCmd = Get-Command pwsh.exe -ErrorAction SilentlyContinue
    if ($pwshCmd -and -not $env:MUD_PSSA_NO_RECURSE) {
        Write-Host "Using PowerShell 7 (pwsh) for PSScriptAnalyzer (Windows PowerShell gallery modules unavailable)." -ForegroundColor Cyan
        $env:MUD_PSSA_NO_RECURSE = '1'
        & $pwshCmd.Path -NoProfile -ExecutionPolicy Bypass -File $PSCommandPath
        exit $LASTEXITCODE
    }
}

# Merge Machine and User PATH (same pattern as hadolint/shellcheck scripts)
foreach ($scope in @('Machine', 'User')) {
    $extra = [Environment]::GetEnvironmentVariable('Path', $scope)
    if ($extra) {
        $env:Path = $env:Path + ';' + $extra
    }
}

function Import-PSScriptAnalyzerModule {
    $already = Get-Module -Name PSScriptAnalyzer
    if ($already) {
        return
    }
    Import-Module PSScriptAnalyzer -ErrorAction SilentlyContinue
    if (Get-Module -Name PSScriptAnalyzer) {
        return
    }

    $available = Get-Module -ListAvailable -Name PSScriptAnalyzer | Sort-Object Version -Descending | Select-Object -First 1
    if ($available) {
        Import-Module $available.Path -Force -ErrorAction Stop
        return
    }

    Write-Host "Installing PSScriptAnalyzer module (CurrentUser)..." -ForegroundColor Cyan
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    try {
        Import-Module PackageManagement -Force -ErrorAction Stop
    } catch {
        Write-Host "ERROR: PackageManagement could not be loaded: $_" -ForegroundColor Red
        Write-Host "Install PowerShell 7: winget install Microsoft.PowerShell" -ForegroundColor Yellow
        Write-Host "Then run: pwsh -File `"$PSCommandPath`"" -ForegroundColor Yellow
        exit 1
    }
    try {
        Import-Module PowerShellGet -Force -ErrorAction Stop
    } catch {
        Write-Host "ERROR: PowerShellGet could not be loaded: $_" -ForegroundColor Red
        Write-Host "Install PowerShell 7: winget install Microsoft.PowerShell" -ForegroundColor Yellow
        Write-Host "Then run: pwsh -File `"$PSCommandPath`"" -ForegroundColor Yellow
        exit 1
    }

    Install-Module -Name PSScriptAnalyzer -Scope CurrentUser -Force -AllowClobber -Repository PSGallery -ErrorAction Stop
    Import-Module PSScriptAnalyzer -Force -ErrorAction Stop
}

try {
    Import-PSScriptAnalyzerModule
} catch {
    Write-Host "ERROR: Could not install or import PSScriptAnalyzer: $_" -ForegroundColor Red
    Write-Host "Try: pwsh -File `"$PSCommandPath`"   or   Install-Module PSScriptAnalyzer -Scope CurrentUser -Force" -ForegroundColor Yellow
    exit 1
}

if (-not (Get-Command Invoke-ScriptAnalyzer -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Invoke-ScriptAnalyzer is not available after importing PSScriptAnalyzer." -ForegroundColor Red
    exit 1
}

Write-Host "Running PSScriptAnalyzer on PowerShell scripts..." -ForegroundColor Cyan
Write-Host "This will check for PowerShell best practices..." -ForegroundColor Gray

$repoRoot = Split-Path -Parent $PSScriptRoot
$scriptsDir = Join-Path $repoRoot "scripts"

$ps1Files = Get-ChildItem -Path $scriptsDir -Filter "*.ps1" -Recurse -ErrorAction SilentlyContinue

if ($ps1Files.Count -eq 0) {
    Write-Host "[WARNING] No .ps1 files found in scripts directory" -ForegroundColor Yellow
    exit 0
}

$success = $true
foreach ($file in $ps1Files) {
    try {
        $results = Invoke-ScriptAnalyzer -Path $file.FullName -Severity Error, Warning -ExcludeRule PSAvoidUsingWriteHost
        if ($results.Count -gt 0) {
            Write-Host "[WARNING] PSScriptAnalyzer found issues in $($file.Name):" -ForegroundColor Yellow
            $results | Format-Table -AutoSize
            $success = $false
        }
    } catch {
        Write-Host "[ERROR] Error running PSScriptAnalyzer on $($file.Name): $_" -ForegroundColor Red
        $success = $false
    }
}

if (-not $success) {
    exit 1
}

Write-Host ""
Write-Host "[SUCCESS] All PSScriptAnalyzer checks passed!" -ForegroundColor Green
