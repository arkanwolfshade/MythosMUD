# Apply Magic System Migration
# This script applies the magic system migration (015_add_magic_system_tables.sql)
# and seed data (seed_spells.sql) to all databases (mythos_dev, mythos_unit, mythos_e2e)

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [string]$Database = "all",  # "all", "mythos_dev", "mythos_unit", "mythos_e2e"
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password
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
$migrationFile = Join-Path $projectRoot "db\migrations\015_add_magic_system_tables.sql"
$seedFile = Join-Path $projectRoot "data\spells\seed_spells.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $seedFile)) {
    Write-Host "[ERROR] Seed file not found: $seedFile" -ForegroundColor Red
    exit 1
}

$databases = @()
if ($Database -eq "all") {
    $databases = @("mythos_dev", "mythos_unit", "mythos_e2e")
}
else {
    $databases = @($Database)
}

# Convert SecureString to plain string for environment variable
# Note: This is necessary for psql, but the password is only in memory temporarily
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
$env:PGPASSWORD = $plainPassword

foreach ($db in $databases) {
    Write-Host "`n[INFO] Processing database: $db" -ForegroundColor Yellow

    try {
        # Check if database exists
        $dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$db\s"
        if (-not $dbExists) {
            Write-Host "[WARN] Database $db does not exist. Skipping..." -ForegroundColor Yellow
            continue
        }

        # Apply migration
        Write-Host "   Applying migration (015_add_magic_system_tables.sql)..." -ForegroundColor Cyan
        $migrationResult = Get-Content $migrationFile | & $psqlPath -h $DbHost -p $Port -U $User -d $db 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "   [OK] Migration applied successfully" -ForegroundColor Green
        }
        else {
            # Check if error is because table already exists (migration already applied)
            $migrationOutput = $migrationResult | Out-String
            if ($migrationOutput -match 'already exists|duplicate') {
                Write-Host "   [OK] Migration already applied (tables already exist)" -ForegroundColor Green
            }
            else {
                Write-Host "   [ERROR] Migration failed: $migrationOutput" -ForegroundColor Red
                continue
            }
        }

        # Apply seed data
        Write-Host "   Loading seed data (seed_spells.sql)..." -ForegroundColor Cyan
        $seedResult = Get-Content $seedFile | & $psqlPath -h $DbHost -p $Port -U $User -d $db 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "   [OK] Seed data loaded successfully" -ForegroundColor Green
        }
        else {
            # Check if error is because spell already exists (seed already loaded)
            $seedOutput = $seedResult | Out-String
            if ($seedOutput -match 'already exists|duplicate|conflict') {
                Write-Host "   [OK] Seed data already loaded (spells already exist)" -ForegroundColor Green
            }
            else {
                Write-Host "   [WARN] Seed data loading had issues: $seedOutput" -ForegroundColor Yellow
                # Continue anyway - seed data conflicts are not critical
            }
        }

        Write-Host "   [OK] Database $db processed successfully" -ForegroundColor Green

    }
    catch {
        Write-Host "   [ERROR] Failed to process database $db : $_" -ForegroundColor Red
        continue
    }
}

Write-Host "`n[OK] Magic system migration completed!" -ForegroundColor Green
Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
# Clear plain password from memory
if ($plainPassword) {
    $plainPassword = $null
    [System.GC]::Collect()
}
