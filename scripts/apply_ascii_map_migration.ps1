# Apply ASCII Map Migration
# This script applies the ASCII map migration (017_add_ascii_map_fields.sql)
# to all databases (mythos_dev, mythos_unit, mythos_e2e)

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$Database = "all",  # "all", "mythos_dev", "mythos_unit", "mythos_e2e"
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force)
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

    $found = $false
    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            $found = $true
            break
        }
    }

    if (-not $found) {
        Write-Host "[ERROR] psql not found. Please install PostgreSQL or specify the path." -ForegroundColor Red
        exit 1
    }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$migrationFile = Join-Path $projectRoot "db\migrations\017_add_ascii_map_fields.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

$databases = @()
if ($Database -eq "all") {
    $databases = @("mythos_dev", "mythos_unit", "mythos_e2e")
}
else {
    $databases = @($Database)
}

# Convert SecureString to plain text for environment variable
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

foreach ($db in $databases) {
    Write-Host "`n[INFO] Processing database: $db" -ForegroundColor Yellow

    try {
        # Check if database exists
        $dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$db\s"
        if (-not $dbExists) {
            Write-Host "[WARN] Database $db does not exist. Skipping..." -ForegroundColor Yellow
            continue
        }

        # Check if migration already applied by checking for columns
        Write-Host "   Checking if migration already applied..." -ForegroundColor Cyan
        $checkQuery = "SELECT column_name FROM information_schema.columns WHERE table_name = 'rooms' AND column_name IN ('map_origin_zone', 'map_symbol', 'map_style')"
        $existingColumns = & $psqlPath -h $DbHost -p $Port -U $User -d $db -t -c $checkQuery 2>&1 | Where-Object { $_ -match '\S' }

        if ($existingColumns -and ($existingColumns | Measure-Object -Line).Lines -eq 3) {
            Write-Host "   [OK] Migration already applied (columns already exist)" -ForegroundColor Green
            continue
        }

        # Apply migration
        Write-Host "   Applying migration (017_add_ascii_map_fields.sql)..." -ForegroundColor Cyan
        $migrationResult = Get-Content $migrationFile | & $psqlPath -h $DbHost -p $Port -U $User -d $db 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "   [OK] Migration applied successfully" -ForegroundColor Green
        }
        else {
            # Check if error is because column already exists (migration already applied)
            $migrationOutput = $migrationResult | Out-String
            if ($migrationOutput -match 'already exists|duplicate') {
                Write-Host "   [OK] Migration already applied (columns already exist)" -ForegroundColor Green
            }
            else {
                Write-Host "   [ERROR] Migration failed: $migrationOutput" -ForegroundColor Red
                continue
            }
        }

    }
    catch {
        Write-Host "   [ERROR] Unexpected error: $_" -ForegroundColor Red
        continue
    }
}

Write-Host "`n=== Migration Complete ===" -ForegroundColor Cyan
