# DEPRECATED: Apply Magic System Migration
# This script is deprecated. The migration (015_add_magic_system_tables.sql) and seed file
# (data/spells/seed_spells.sql) have been removed. Schema and spell data are now in authoritative
# DDL (db/mythos_*_ddl.sql) and DML (data/db/mythos_*_dml.sql). Use scripts/load_world_seed.py or
# apply the appropriate mythos_*_ddl.sql and mythos_*_dml.sql for your environment.

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

# Deprecation: exit with instructions (migration and seed files no longer exist)
Write-Host "[DEPRECATED] This script applied 015_add_magic_system_tables.sql and seed_spells.sql." -ForegroundColor Yellow
Write-Host "Those files have been removed. Use authoritative DDL and DML instead:" -ForegroundColor Yellow
Write-Host "  - DDL: db/mythos_dev_ddl.sql, db/mythos_unit_ddl.sql, db/mythos_e2e_ddl.sql" -ForegroundColor Cyan
Write-Host "  - DML: data/db/mythos_dev_dml.sql, mythos_unit_dml.sql, mythos_e2e_dml.sql" -ForegroundColor Cyan
Write-Host "  - Full reset: CONFIRM_LOAD_WORLD_SEED=1 python scripts/load_world_seed.py" -ForegroundColor Cyan
exit 1

# PostgreSQL psql executable path (unreachable; script deprecated)
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
