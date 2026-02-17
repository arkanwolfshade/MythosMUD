# Apply Migration 022: Heal Self / Heal Other rename (clerical_basic_heal -> heal_self, clerical_minor_heal -> heal_other)
#
# Usage:
#   .\scripts\apply_022_heal_self_heal_other_rename.ps1 -Database "mythos_dev"
#   .\scripts\apply_022_heal_self_heal_other_rename.ps1 -Database "mythos_unit"
#   .\scripts\apply_022_heal_self_heal_other_rename.ps1 -Database "mythos_e2e"

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force),
    [string]$Database = "mythos_dev",
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

Write-Host "=== Migration 022: Heal Self / Heal Other Rename ===" -ForegroundColor Cyan
Write-Host ""

# Find psql executable
$psqlPath = Get-Command psql -ErrorAction SilentlyContinue
if (-not $psqlPath) {
    $commonPaths = @(
        "E:\Program Files\PostgreSQL\18\bin\psql.exe",
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe"
    )
    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            break
        }
    }
    if (-not $psqlPath) {
        Write-Host "[ERROR] psql not found. Please install PostgreSQL or specify the path." -ForegroundColor Red
        exit 1
    }
}
else {
    $psqlPath = $psqlPath.Path
}

Write-Host "[INFO] Using psql: $psqlPath" -ForegroundColor Cyan

# Set PostgreSQL password
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

# Get migration file path
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$migrationFile = Join-Path $projectRoot "data\db\migrations\10_heal_self_heal_other_rename.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

# Check if database exists
Write-Host "[INFO] Checking if database exists..." -ForegroundColor Yellow
$dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$Database\s"
if (-not $dbExists) {
    Write-Host "[ERROR] Database $Database does not exist!" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Database $Database exists" -ForegroundColor Green
Write-Host ""

if ($DryRun) {
    Write-Host "[DRY RUN] Would apply migration to $Database" -ForegroundColor Yellow
    Write-Host "[DRY RUN] Migration file: $migrationFile" -ForegroundColor Yellow
    exit 0
}

# Apply migration
Write-Host "[INFO] Applying migration: 10_heal_self_heal_other_rename.sql" -ForegroundColor Yellow
Write-Host ""

try {
    $process = Start-Process -FilePath $psqlPath -ArgumentList @(
        "-h", $DbHost,
        "-p", $Port,
        "-U", $User,
        "-d", $Database,
        "-f", $migrationFile,
        "-v", "ON_ERROR_STOP=1"
    ) -NoNewWindow -Wait -PassThru -RedirectStandardOutput "temp_stdout_022.txt" -RedirectStandardError "temp_stderr_022.txt"

    $exitCode = $process.ExitCode
    $stdoutContent = Get-Content "temp_stdout_022.txt" -ErrorAction SilentlyContinue | Out-String
    $stderrContent = Get-Content "temp_stderr_022.txt" -ErrorAction SilentlyContinue | Out-String

    Remove-Item "temp_stdout_022.txt" -ErrorAction SilentlyContinue
    Remove-Item "temp_stderr_022.txt" -ErrorAction SilentlyContinue

    if ($exitCode -eq 0) {
        if ($stderrContent -and $stderrContent -notmatch '^NOTICE:') {
            Write-Host "[WARNING] Migration completed but had warnings:" -ForegroundColor Yellow
            Write-Host $stderrContent -ForegroundColor Yellow
        }
        Write-Host "[OK] Migration 10 (heal_self/heal_other rename) applied successfully" -ForegroundColor Green
        Write-Host "[INFO] Verifying spells..." -ForegroundColor Yellow
        $verifyResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -c "SELECT spell_id, name FROM spells WHERE spell_id IN ('heal_self','heal_other') ORDER BY spell_id;" 2>&1
        Write-Host $verifyResult
        Write-Host ""
        Write-Host "[SUCCESS] Migration 10 (heal_self/heal_other rename) completed!" -ForegroundColor Green
    }
    else {
        Write-Host "[ERROR] Migration failed with exit code $exitCode" -ForegroundColor Red
        if ($stderrContent) { Write-Host "Error output:" -ForegroundColor Red; Write-Host $stderrContent -ForegroundColor Red }
        if ($stdoutContent) { Write-Host "Standard output:" -ForegroundColor Yellow; Write-Host $stdoutContent -ForegroundColor Yellow }
        exit 1
    }
}
catch {
    Write-Host "[ERROR] Error applying migration: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Migration Complete ===" -ForegroundColor Cyan
