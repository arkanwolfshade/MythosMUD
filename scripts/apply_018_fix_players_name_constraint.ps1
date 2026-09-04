# Apply Migration 018: Fix Players Name Constraint
# This script drops the old players_new_name_key constraint that prevents
# deleted character names from being reused

# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force),
    [string]$Database = "mythos_dev"
)

$ErrorActionPreference = "Stop"

# PostgreSQL psql executable path
$psqlPath = "E:\Program Files\PostgreSQL\18\bin\psql.exe"

if (-not (Test-Path $psqlPath)) {
    # Try to find psql in common locations
    $commonPaths = @(
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe",
        "E:\Program Files\PostgreSQL\*\bin\psql.exe"
    )

    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            break
        }
    }

    if (-not (Test-Path $psqlPath)) {
        Write-Host "[ERROR] psql not found. Please install PostgreSQL or specify the path." -ForegroundColor Red
        exit 1
    }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$migrationFile = Join-Path $projectRoot "db\migrations\018_fix_players_name_constraint.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

# Set PostgreSQL password
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

Write-Host "=== Applying Migration 018: Fix Players Name Constraint ===" -ForegroundColor Cyan
Write-Host "Database: $Database" -ForegroundColor Cyan
Write-Host ""

# Check if database exists
$dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$Database\s"
if (-not $dbExists) {
    Write-Host "[ERROR] Database '$Database' does not exist" -ForegroundColor Red
    exit 1
}

# Check if constraint exists before migration
Write-Host "Checking if constraint exists..." -ForegroundColor Yellow
$checkQuery = "SELECT 1 FROM pg_constraint WHERE conname = 'players_new_name_key';"
$constraintExists = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -c $checkQuery 2>&1 | Where-Object { $_ -match '1' }

if ($constraintExists) {
    Write-Host "[INFO] Constraint 'players_new_name_key' found, will be dropped" -ForegroundColor Yellow
}
else {
    Write-Host "[INFO] Constraint 'players_new_name_key' not found (may already be dropped)" -ForegroundColor Yellow
}

# Apply migration
Write-Host "Applying migration..." -ForegroundColor Yellow
$migrationResult = Get-Content $migrationFile | & $psqlPath -h $DbHost -p $Port -U $User -d $Database 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Migration applied successfully" -ForegroundColor Green

    rify constraint was dropped
    $constraintStillExists = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -c $checkQuery 2>&1 | Where-Object { $_ -match '1' }
    if (-not $constraintStillExists) {
        Write-Host "[OK] Constraint 'players_new_name_key' successfully dropped" -ForegroundColor Green
    }
    else {
        Write-Host "[WARNING] Constraint 'players_new_name_key' still exists" -ForegroundColor Yellow
    }
}
else {
    Write-Host "[ERROR] Migration failed" -ForegroundColor Red

    Write-Host $migrationResult -ForegroundColor Red
    exit 1


    W
    rit e-Host ""

    Write-Host ""

    Write-Host ""Write-Host ""
    Write-Host ""
    Write-Host "=== Migration Complete ===" -ForegroundColor Cyan
